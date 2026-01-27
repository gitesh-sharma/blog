---
layout: default
title: Blog Posts
---

{% for post in site.posts %}
<a class="post-card" href="{{ site.baseurl }}{{ post.url }}">
  <h3>{{ post.title }}</h3>
  <span>{{ post.date | date: "%d %b %Y" }}</span>
</a>
{% endfor %}
