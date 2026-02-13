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

# Get the title from a post
get_title() {
    local file="$1"
    grep -m1 '^title:' "$file" | sed 's/title: *"//' | sed 's/"$//'
}

# Check if title appears to violate title case
# Returns 0 if valid, 1 if suspicious
# Checks: words after first that start lowercase (excluding articles/prepositions)
check_title_case() {
    local file="$1"
    local title=$(get_title "$file")

    if [[ -z "$title" ]]; then
        return 0
    fi

    # Skip words that are allowed to be lowercase (articles, short prepositions, conjunctions)
    local skip_words="a an the and but or nor for yet so in on at to by of as"

    # Check each word after the first
    local first=1
    for word in $title; do
        if [[ $first -eq 1 ]]; then
            first=0
            # First word must be capitalized
            if [[ "$word" =~ ^[a-z] ]]; then
                return 1
            fi
            continue
        fi

        # Skip allowed lowercase words
        local lower_word=$(echo "$word" | tr '[:upper:]' '[:lower:]')
        if [[ " $skip_words " =~ " $lower_word " ]]; then
            continue
        fi

        # Check if word starts with lowercase
        if [[ "$word" =~ ^[a-z] ]]; then
            return 1
        fi
    done

    return 0
}
