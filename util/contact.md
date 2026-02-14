---
layout: container
title: Contact
permalink: "/contact"
---

Please use the form below to get in touch with me. I will do my best to respond to your message as soon as possible. (This form is powered by Netlify Forms; if you are accessing this website via the [Github Pages mirror](https://roelchristian.github.io/), the form will not work.)
{: .mt-5 .mb-4 .col-lg-6}

<div class="row mb-5">
  <div class="col-12 col-lg-7 col-xl-6">
    <div class="p-0">
      <form name="contact"
            method="POST"
            action="/thanks"
            data-netlify="true"
            netlify-honeypot="bot-field">
        <input type="hidden" name="contact-form" value="contact">
        <p class="d-none">
          <label>Don’t fill this out if you’re human: <input name="bot-field"></label>
        </p>
        <div class="mb-3">
          <label for="name" class="form-label ">Name</label>
          <input type="text"
                 name="name"
                 id="name"
                 class="form-control rounded-0"
                 required>
        </div>
        <div class="mb-3">
          <label for="email" class="form-label mb-1">Email</label>
          <input type="email"
                 name="_replyto"
                 id="email"
                 class="form-control rounded-0"
                 required>
          <div class="form-text">This helps prevent spam. I will only use this to reply.</div>
        </div>
        <div class="mb-3">
          <label for="message" class="form-label mb-1">Message</label>
          <textarea name="message"
                    id="message"
                    rows="6"
                    class="form-control rounded-0"
                    required></textarea>
        </div>
        <div class="d-flex align-items-center gap-3 mt-4">
          <button type="submit" class="btn btn-outline-dark rounded-0 px-4">
            Send
          </button>
        </div>
        <hr class="my-4">
        <p class="small text-body-secondary mb-0">
          By using this website and/or submitting this form, you agree to the
          <a href="/terms" class="link-secondary">terms of service</a>
          of this website.
        </p>
      </form>
    </div>
  </div>
</div>