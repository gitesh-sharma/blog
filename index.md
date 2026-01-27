---
layout: default
title: Blog
---
<h1>Sharmaji Blog 🚀</h1>
<p>Latest articles on SEO, tools, and technology.</p>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ site.baseurl }}{{ post.url }}">
        {{ post.title }}
      </a>
      <small> – {{ post.date | date: "%d %b %Y" }}</small>
    </li>
  {% endfor %}
</ul>
