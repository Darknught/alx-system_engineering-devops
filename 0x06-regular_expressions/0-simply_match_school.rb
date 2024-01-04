#!/usr/bin/env ruby
# A script that accepts one arg and pass it to a regular exp matching method

puts ARGV[0].scan(/School/).join
