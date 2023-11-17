### Introduction

When a client makes a first request, the server can attach one or more cookies to its response. The client can then send these cookies back with future requests to maintain a state between two requests. Cookies have attributes that define several criteria like lifespan, domain, conditions of sending, etc.

The `HttpOnly` attribute limits the scope of the cookie to HTTP requests. In particular, this attribute tells the user agent to omit the cookie when accessing cookies via non-HTTP APIs (such as a web browser API that exposes cookies to scripts). It helps to limit access and modification of the cookie.

### Procedure

Upon inspecting the page, it was found that the 'I_am_admin' cookie lacks protection by the 'HttpOnly' attributes. Changing the value to true in md5 displays the flag.

### How to Fix

To address the security issue related to the 'HttpOnly' attribute missing from cookies, follow these steps:

1. **Server-Side Script Adjustment:** Modify the server-side script to set the `HttpOnly` attribute for every cookie.

2. **Secure Cookie Attributes:** Ensure that all cookies have secure attributes set, including `Secure`, `HttpOnly`, and `SameSite`. The `Secure` attribute ensures cookies are sent over HTTPS, while `SameSite` can be used to control cross-site usage.

### Source

[OWASP - HttpOnly](https://owasp.org/www-community/HttpOnly)