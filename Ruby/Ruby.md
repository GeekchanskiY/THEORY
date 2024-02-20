
**Documentation**
https://www.ruby-lang.org/en/documentation/

[[Rails]]
[[OOP in Ruby]]
[[Ruby/RSpec]]
[[Ruby tips, hints and tricks]]
[[Modules in Ruby]]

### Data types
- [[Ruby numbers]]
- [[Ruby booleans]]
- [[Ruby strings]] #TODO frozen string
- [[Ruby hashes]]
- [[Ruby arrays]]
- [[Ruby symbols]]

```ruby
# Ruby program to illustrate the
# Hashes Data Type

#!/usr/bin/ruby
hsh = colors = { "red" => 0xf00, "green" => 0x0f0, "blue" => 0x00f }
hsh.each do |key, value|
print key, " is ", value, "\n"
end

```

**Symbols:** Symbols are light-weight strings. A symbol is preceded by a colon (:). They are used instead of strings because they can take up much less memory. Symbols have better performance.

```ruby
# Ruby program to illustrate the
# Symbols Data Type

#!/usr/bin/ruby
domains = {:sk => "GeeksforGeeks", :no => "GFG", :hu => "Geeks"}

puts domains[:sk]
puts domains[:no]
puts domains[:hu]

```
Symbols also are also used for different purpose than string
Detail info: https://www.rubyguides.com/2018/02/ruby-symbols/


### Working with strings:
sub/gsub to replace character or all of them

replace to replace all the string

