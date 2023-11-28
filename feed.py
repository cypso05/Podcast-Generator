import yaml
import xml.etree.ElementTree as xml_tree
# importing yaml and xaml functions and then veryfying that our file is opened correctly. 
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load (file)

    # creating the RSS element 
    rss_element = xml_tree.Element('rss', {'version':'2.0',
 'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd', 
 'xmlns:content':'http://purl.org/rss/1.0/modules/content/'})

 # create element for the channels 
    channel_element = xml_tree.SubElement(rss_element, 'channel')
       
 # add a link
link_prefix = yaml_data['link'] 

# converting xml to yaml data
xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']
xml_tree.SubElement(channel_element, 'format').text = yaml_data['format']
xml_tree.SubElement(channel_element, 'subtitle').text = yaml_data['subtitle']
xml_tree.SubElement(channel_element, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channel_element, 'description').text = yaml_data['description']
xml_tree.SubElement(channel_element, 'itunes:image', {'href':link_prefix +  yaml_data['image']})
xml_tree.SubElement(channel_element, 'lanuguage').text = yaml_data['language']
xml_tree.SubElement(channel_element, 'link').text = link_prefix
xml_tree.SubElement(channel_element, 'itunes:category', {'text': yaml_data['category'] })

#creating items, a sort of container for episodes
for item in yaml_data['item']: 
    item_element = xml_tree.SubElement(channel_element, 'item')
    xml_tree.SubElement(item_element, 'title').text = item ['title']
    xml_tree.SubElement(item_element, 'itunes:author').text = yaml_data ['author']
    xml_tree.SubElement(item_element, 'description').text = item ['description']
    xml_tree.SubElement(item_element, 'itunes:duration').text = item ['duration']
    xml_tree.SubElement(item_element, 'pubDate').text = item ['published']
    xml_tree.SubElement(item_element, 'title').text = item ['title']

    enclosure = xml_tree.SubElement(item_element, 'enclosure', {
        'url': link_prefix + item['file'],
        'type' : 'audio/mpeg',
        'length': item['length'] })



#setting up the output.
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xaml', encoding = 'UTF-8', xml_declaration=True)


  
