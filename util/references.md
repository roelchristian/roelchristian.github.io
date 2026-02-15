---
layout: post
title: Citations and references
permalink: references
---

{% assign refs = site.data.references %}

{%- assign sort_keys = "" | split: "" -%}
{%- for r in refs -%}
  {%- comment -%} pick an author sort string {%- endcomment -%}
  {%- if r.authors and r.authors.size > 0 -%}
    {%- assign author_sort = r.authors[0].name_sort | default: r.authors[0].name | default: "" -%}
  {%- else -%}
    {%- assign author_sort = r.author_sort | default: r.author | default: "" -%}
  {%- endif -%}

  {%- assign author_sort = author_sort | strip | downcase -%}
  {%- assign title_sort  = r.title | default: "" | strip | downcase -%}

  {%- comment -%}
    If author_sort is blank, it will sort FIRST. If you want those LAST, replace "" with "zzzzzz".
  {%- endcomment -%}
  {%- if author_sort == "" -%}
    {%- assign author_sort = "zzzzzz" -%}
  {%- endif -%}

  {%- capture k -%}{{ author_sort }}||{{ title_sort }}||{{ r.key }}{%- endcapture -%}
  {%- assign sort_keys = sort_keys | push: k -%}
{%- endfor -%}

{%- assign sort_keys = sort_keys | sort -%}

<ul class="refs">
{%- for k in sort_keys -%}
  {%- assign parts = k | split: "||" -%}
  {%- assign ref_key = parts[2] -%}
  {%- assign ref = refs | where: "key", ref_key | first -%}

  {%- capture author_display -%}
    {%- if ref.authors and ref.authors.size > 0 -%}
      {%- assign n = ref.authors.size -%}
      {%- assign a1 = ref.authors[0].name | default: "" | strip -%}
      {%- assign a2 = ref.authors[1].name | default: "" | strip -%}
      {%- if n == 1 -%}
        {{ a1 }}
      {%- elsif n == 2 -%}
        {{ a1 }} &amp; {{ a2 }}
      {%- else -%}
        {{ a1 }} <em>et al.</em>
      {%- endif -%}
    {%- else -%}
      {{ ref.author | default: "" | strip }}
    {%- endif -%}
  {%- endcapture -%}

  {%- capture translator_display -%}
    {%- if ref.translators and ref.translators.size > 0 -%}
      {%- assign tn = ref.translators.size -%}
      {%- assign t1 = ref.translators[0].name | default: "" | strip -%}
      {%- assign t2 = ref.translators[1].name | default: "" | strip -%}
       <em> trans. </em>
     
      {%- if tn == 1 -%}
        {{ t1 }}
      {%- elsif tn == 2 -%}
        {{ t1 }} &amp; {{ t2 }}
      {%- else -%}
        {{ t1 }} <em>et al.</em>
      {%- endif -%}
    {%- endif -%}
  {%- endcapture -%}

  {% assign title = ref.title | default: "Untitled" | strip %}

  {% if ref.publication_year_display %}
    {% assign year = ref.publication_year_display %}
  {% else %}
    {% assign year = ref.publication_year | default: "n.d." %}
  {% endif %}

  {% assign trans_year = ref.translation_year | default: "" %}
  {% assign url = ref.url | default: "" | strip %}

  <li id="{{ ref.key }}">
    {%- if author_display != "" -%}
      {{ author_display | strip }}.
    {%- endif -%}

    {% if url != "" %}
      <a href="{{ url }}" target="_blank" rel="noopener">
        <cite>{{ title }}.</cite>
      </a>
    {% else %}
      <cite>{{ title }}.</cite>
    {% endif %}

    {% if year != "n.d." %} {{ year }}.{% endif %}

    {%- if translator_display != "" -%}
      {{ translator_display }}.
    {%- endif -%}

    {% if trans_year != "" %} {{ trans_year }}.{% endif %}
  </li>

{%- endfor -%}
</ul>
