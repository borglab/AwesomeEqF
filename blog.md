---
layout: default
title: Blog
permalink: /blog/
---

# Blog

Welcome to the AwesomeEqF blog! Here you'll find tutorials, insights, and updates about invariant and equivariant filtering.

{% for post in site.posts %}
  <article class="post">
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="post-meta">
      {{ post.date | date: "%B %d, %Y" }}
      {% if post.author %} • {{ post.author }}{% endif %}
      {% if post.categories %} • {{ post.categories | join: ', ' }}{% endif %}
    </p>
    <div class="post-excerpt">
      {{ post.excerpt }}
    </div>
    <a href="{{ post.url | relative_url }}">Read more →</a>
  </article>
  <hr>
{% endfor %}

{% if site.posts.size == 0 %}
  <p>No posts yet. Check back soon for tutorials and insights on invariant and equivariant filtering!</p>
{% endif %}
