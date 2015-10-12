Warmup:
Used Content Security Policy. Add response.headers['Content-Security-Policy'] = "script-src 'self'" so that injected script will not able to be executed. Moved the javascript to assets/javascript so that only these javascript can be executed. 

A:
The server should not put username in the cookie along. Either put some security token belongs only to the specific user in the cookie, or hash the username to some other value that can't be guessed by the attacker in the cookie to identify the user will be a better way. The server should then check if the token or the hashed username is correct by comparing the received token or hashed username with the token in the database or with the hash function. The token or the hashed value should not only depend on the username, should be different each time to avoid the attacker to try it thousands of time to guess the value.  
Referenced: http://www.html5rocks.com/en/tutorials/security/content-security-policy/

In addition, I don't think the attacker can easily get the security token of the website. Protecting the security token will be another thing that this website need to do in order to defense attack A.

B:
In the form, I added a hidden field which contains a security token session[:token]. This token becomes different each time. When post_transfer, it will compare the submitted token with the true token in order to verify if it is not a CSRF. It will return an error message if the security token is not correct.

B+:
I used the method described in the paper http://crypto.stanford.edu/~dabo/pubs/papers/framebust.pdf to fight against framebusting. I make the website invisible by default. If the website is contained in a frame, I will make the whole page to be my webpage. If this fails (maybe achieved by sandbox), my website will be invisible so that the attacker cann't make the user to do anything bad. 

C:
I first change the destroy user to a safer version. User.find_by_username(@username).destroy(). Thus, the username will be escaped by the ruby framework. 

In addition to that, I add a validation for the username in the register process. The username is restricted to A-Z, a-z, 0-9, and underscore by using regular expression match. Thus, the equal sign will not be allowed in the username and the sql will not be able to execute.

D:
It is so dangerous to use eval because the attacker will have a lot of opportunities to do. Thus, I used parseInt instead to get the number of bitbars. In the setInterval, I didn't use string to call the method directly. I used function(){} to call my function.

In addition, I remote id and class from sanitize(profile, tags: %w(a br b h1 h2 h3 h4 i img li ol p strong table tr td th u ul em span), attributes: %w(href colspan rowspan src align valign)) so that the attacker will not be able to set my id and class.

E:
First, I replace the form with Ruby on Rails's form_tag. Thus, the input value will not be considered as a class or id or any event handler. Ruby on Rails's form_tag is safer than the html form. Thus, the attacker will not be able to inject any code and execute it. 

Second, I escaped the error message using error_msg = CGI.escapeHTML(error_msg) so that the script in the user name will not be able to executed.

Third, I enabled CSP so that the script will not be able to executed.

In addition, since I added the limitation of the username described in attack C, the validation mechnism reject the username immediately.
