#!/bin/bash

# Unit tests for post-checks.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/../lib/post-checks.sh"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

passed=0
failed=0

# Test helper
run_test() {
    local name="$1"
    local expected="$2"  # "pass" or "fail"
    local result="$3"    # 0 for pass, 1 for fail

    if [[ "$expected" == "pass" && "$result" -eq 0 ]] || \
       [[ "$expected" == "fail" && "$result" -ne 0 ]]; then
        echo "✓ $name"
        ((passed++))
    else
        echo "✗ $name (expected $expected)"
        ((failed++))
    fi
}

# Create test fixtures
create_post() {
    local name="$1"
    local content="$2"
    echo "$content" > "$TEMP_DIR/$name.md"
    echo "$TEMP_DIR/$name.md"
}

echo "=== Timezone Tests ==="

# Test: Valid GMT timezone
file=$(create_post "valid-tz" "---
layout: post
title: Test
date: 2026-01-08 09:00:00 +0000
---
Content")
check_timezone "$file"
run_test "Valid GMT timezone (+0000)" "pass" $?

# Test: Wrong timezone (BST)
file=$(create_post "wrong-tz-bst" "---
layout: post
title: Test
date: 2026-01-08 09:00:00 +0100
---
Content")
check_timezone "$file"
run_test "Wrong timezone (+0100) should fail" "fail" $?

# Test: Wrong timezone (US Eastern)
file=$(create_post "wrong-tz-us" "---
layout: post
title: Test
date: 2026-01-08 09:00:00 -0500
---
Content")
check_timezone "$file"
run_test "Wrong timezone (-0500) should fail" "fail" $?

# Test: No timezone specified
file=$(create_post "no-tz" "---
layout: post
title: Test
date: 2026-01-08 09:00:00
---
Content")
check_timezone "$file"
run_test "No timezone specified should fail" "fail" $?

# Test: No date line at all
file=$(create_post "no-date" "---
layout: post
title: Test
---
Content")
check_timezone "$file"
run_test "No date line should pass (skip)" "pass" $?

echo ""
echo "=== Future Date Tests ==="

# Use a fixed "now" for reproducible tests: 2026-01-08 10:00:00 UTC
FIXED_NOW=$(date -u -j -f "%Y-%m-%d %H:%M:%S" "2026-01-08 10:00:00" +%s)

# Test: Past date
file=$(create_post "past-date" "---
layout: post
title: Test
date: 2026-01-08 09:00:00 +0000
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "Past date should pass" "pass" $?

# Test: Future date (1 hour ahead)
file=$(create_post "future-date" "---
layout: post
title: Test
date: 2026-01-08 11:00:00 +0000
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "Future date should fail" "fail" $?

# Test: Future date with override
file=$(create_post "future-override" "---
layout: post
title: Test
date: 2026-01-08 11:00:00 +0000
future: true
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "Future date with 'future: true' should pass" "pass" $?

# Test: Far future date
file=$(create_post "far-future" "---
layout: post
title: Test
date: 2030-01-08 09:00:00 +0000
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "Far future date should fail" "fail" $?

# Test: Exact same time (edge case - should pass)
file=$(create_post "exact-now" "---
layout: post
title: Test
date: 2026-01-08 10:00:00 +0000
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "Exact current time should pass" "pass" $?

# Test: One second in future
FIXED_NOW_MINUS_1=$((FIXED_NOW - 1))
file=$(create_post "one-sec-future" "---
layout: post
title: Test
date: 2026-01-08 10:00:00 +0000
---
Content")
check_not_future "$file" "$FIXED_NOW_MINUS_1"
run_test "One second in future should fail" "fail" $?

echo ""
echo "=== Edge Cases ==="

# Test: Malformed date
file=$(create_post "malformed" "---
layout: post
title: Test
date: not-a-date
---
Content")
check_timezone "$file"
run_test "Malformed date timezone check should fail" "fail" $?

check_not_future "$file" "$FIXED_NOW"
run_test "Malformed date future check should pass (skip)" "pass" $?

# Test: Empty file
file=$(create_post "empty" "")
check_timezone "$file"
run_test "Empty file timezone check should pass (skip)" "pass" $?

check_not_future "$file" "$FIXED_NOW"
run_test "Empty file future check should pass (skip)" "pass" $?

# Test: future: false should NOT override
file=$(create_post "future-false" "---
layout: post
title: Test
date: 2026-01-08 11:00:00 +0000
future: false
---
Content")
check_not_future "$file" "$FIXED_NOW"
run_test "future: false should NOT override (still fail)" "fail" $?

echo ""
echo "=== Results ==="
echo "Passed: $passed"
echo "Failed: $failed"

if [[ $failed -gt 0 ]]; then
    exit 1
fi
exit 0
