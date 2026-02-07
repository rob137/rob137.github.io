#!/bin/bash
# Brutal editor - runs a fresh Claude instance to identify cuts

POST_PATH="$1"

if [ -z "$POST_PATH" ]; then
    echo "Usage: ./scripts/brutal-edit.sh _posts/your-post.md"
    exit 1
fi

if [ ! -f "$POST_PATH" ]; then
    echo "File not found: $POST_PATH"
    exit 1
fi

PROMPT=$(cat << 'EOF'
You are a ruthless editor. Your job is to identify what should be cut from this blog post.

Context:
- These posts are compressed from ~25 minutes of talking
- The writer tends to include too many threads
- The model that helped draft was probably being polite
- You have no such obligation

Instructions:
1. Identify the ONE core argument
2. List everything that doesn't directly serve it
3. Quote specific lines that should go
4. Don't soften recommendations

Output format:
CORE ARGUMENT: [one sentence]

CUT:
- "[quote]" - reason

KEEP: [brief note on what stays]

Be brutal. Interesting ≠ essential. The raw transcript is preserved elsewhere.
EOF
)

POST_CONTENT=$(cat "$POST_PATH")

claude -p "$PROMPT

---

$POST_CONTENT"
