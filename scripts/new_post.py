#!/usr/bin/env python3
"""
Daily Post Generator Script for Sharmaji Blog.
Usage:
    python3 scripts/new_post.py "Your Post Title Here" "Optional Description" "Tag1,Tag2"
"""

import sys
import os
import re
from datetime import datetime

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

def create_daily_post(title, description="Daily update and technical notes.", tags_str="Tech,Blogging"):
    today_str = datetime.now().strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{today_str}-{slug}.md"
    posts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "_posts")

    os.makedirs(posts_dir, exist_ok=True)
    filepath = os.path.join(posts_dir, filename)

    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
        return filepath

    tags_list = [tag.strip() for tag in tags_str.split(",") if tag.strip()]
    formatted_tags = ", ".join(tags_list)

    content = f"""---
layout: post
title: "{title}"
description: {description}
date: {today_str}
author: Gitesh Sharma
tags: [{formatted_tags}]
---

Welcome to today's post!

### Overview
Write your daily post content here...

### Key Takeaways
- Point 1
- Point 2
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully created daily blog post: {filepath}")
    return filepath

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/new_post.py \"Post Title\" [Description] [Tags]")
        sys.exit(1)

    title_arg = sys.argv[1]
    desc_arg = sys.argv[2] if len(sys.argv) > 2 else "Daily update and technical notes."
    tags_arg = sys.argv[3] if len(sys.argv) > 3 else "Tech,Blogging"

    create_daily_post(title_arg, desc_arg, tags_arg)
