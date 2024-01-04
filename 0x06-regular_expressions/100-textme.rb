#!/usr/bin/env ruby
puts ARGV[0].scan(/From: (\w+), To: (\w+), Flags: (\w+)/).join
