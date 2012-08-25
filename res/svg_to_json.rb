require 'nokogiri'
require 'json'
require 'find'
require 'fileutils'

def hash_from_svg(filename)
	doc = Nokogiri::HTML(open(filename))

	rects = {}
	i = 0
	divider = 100.0
	p '-----------------------'
	p '-----------------------'
	p filename
	doc.xpath('//rect').each do |rect|
		key = rect.get_attribute('id') || "rect_#{i}"
		rects[key.to_sym] = {}
		p key
		p "**********BEFORE"
		p rect.get_attribute('width').to_f, rect.get_attribute('height').to_f
		rects[key.to_sym][:width] = (rect.get_attribute('width').to_f)/divider
		rects[key.to_sym][:height] = (rect.get_attribute('height').to_f)/divider
		p "**********AFTER"
		p ""
		p rects[key.to_sym][:width], rects[key.to_sym][:height]
		rects[key.to_sym][:x] =	(rect.get_attribute('x').to_f/divider + rects[key.to_sym][:width]/2)
		rects[key.to_sym][:y] =	(-(rect.get_attribute('y').to_f/divider + rects[key.to_sym][:height]/2))
		
		i+=1
	end
	p '-----------------------'
	p '-----------------------'
	rects
end 


unless ARGV.count < 1
	dir = ARGV[0].split(File::SEPARATOR)
	root = dir.pop + "_json"
	dir = File.join(dir)
	p dir
	absolute = ARGV[1] || Dir.pwd

	# Find all files in sub-directories
	Find.find(dir) do |path|
	p path
		if path.split('.').last == 'svg'
			filename = path.split(File::SEPARATOR).last.split('.').first
			relative = path.split(dir).last.split(File::SEPARATOR).select{|node| !node.empty?}
			relative.pop
			relative = relative.drop(1)
			
			new_path = [absolute, root, relative].flatten
			new_file = [new_path, "#{filename}.json"].flatten
			
			# Create subdirectories for json
			FileUtils.mkpath File.join(new_path)
			
			# Write json
			file = File.open(File.join(new_file), "w+") rescue File.new(File.join(new_file), "w+")
			file.write(JSON.pretty_generate(hash_from_svg(path)))
			file.close
			p "writing : #{File.join(new_file)}"
		end
	end
else
	p "Need parameters : "
	p "svg_to_json.rb [path_to_svg] [path_to_json (optional)]"
end
