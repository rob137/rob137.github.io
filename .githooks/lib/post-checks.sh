#!/bin/bash

# Library of post validation functions
# Sourced by pre-push hook and tests

# Check if a post has GMT timezone
# Returns 0 if valid, 1 if invalid
check_timezone() {
    local file="$1"
    local date_line=$(grep -m1 '^date:' "$file")

    if [[ -z "$date_line" ]]; then
        return 0  # No date line, skip
    fi

    if [[ "$date_line" =~ \+0000 ]]; then
        return 0
    else
        return 1
    fi
}

# Check if a post has a future date
# Returns 0 if valid (not future), 1 if future-dated
# Skips check if 'future: true' is set
check_not_future() {
    local file="$1"
    local current_timestamp="${2:-$(date -u +%s)}"

    # Skip if future: true override is set
    if grep -q '^future: true' "$file"; then
        return 0
    fi

    local date_line=$(grep -m1 '^date:' "$file")

    if [[ -z "$date_line" ]]; then
        return 0  # No date line, skip
    fi

    # Extract datetime: 2026-01-08 09:30:00
    local datetime=$(echo "$date_line" | grep -oE '[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}')

    if [[ -z "$datetime" ]]; then
        return 0  # Can't parse, skip
    fi

    local post_timestamp=$(date -u -j -f "%Y-%m-%d %H:%M:%S" "$datetime" +%s 2>/dev/null)

    if [[ -z "$post_timestamp" ]]; then
        return 0  # Can't parse, skip
    fi

    if [[ "$post_timestamp" -gt "$current_timestamp" ]]; then
        return 1
    fi

    return 0
}

# Get the date line from a post (for error messages)
get_date_line() {
    local file="$1"
    grep -m1 '^date:' "$file"
}
