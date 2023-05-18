import xml.etree.ElementTree as ET

tree = ET.parse('country.xml')
root = tree.getroot()

# 打印根节点的tag
print(root.tag)
# 打印根节点的属性字典
print(root.attrib)

"""
data
{}
"""

# 打印子节点
for child in root:
    print(child.tag, child.attrib)
'''
country {'name': 'Liechtenstein'}
country {'name': 'Singapore'}
country {'name': 'Panama'}
'''

# 子节点是嵌套的，我们可以通过索引访问具体的子节点：
print(root[0][2].text)
print(root[1][2].text)
print(root[2][2].text)
'''
上述访问的是:
<gdppc>141100</gdppc>
<gdppc>59900</gdppc>
<gdppc>13600</gdppc>
'''

# Element有一些有用的方法可以帮助递归迭代它下面的所有子树（它的孩子，他们的孩子，等等）
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)
'''
上面是迭代所有子树的neighbor标签
{'name': 'Austria', 'direction': 'E'}
{'name': 'Switzerland', 'direction': 'W'}
{'name': 'Malaysia', 'direction': 'N'}
{'name': 'Costa Rica', 'direction': 'W'}
{'name': 'Colombia', 'direction': 'E'}
'''

'''
Element.findall()仅查找带有标签的元素
Element.find() :找到第一个带有特定标签的子元素
Element.text:访问标签的内容
Element.get()：访问标签的属性值

'''
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

''' 
修改XML文件

Element.text: 直接更改字段
Element.set: 添加和修改属性
Element.append: 添加新的子对象
'''

''' 
下面例子：
（1）国家排名 + 1
（2）rank元素增加属性
'''
for rank in root.iter('rank'):
    new = int(rank.text) + 1
    rank.text = str(new)
    rank.set('updated', 'yes')

# 上述更改完成后，输出到一个新的xml文件
tree.write('output.xml')


