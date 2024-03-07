class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      result.append(node)
      
      if node['id'] == id:
        return node
      
      if node['children']:
        nodes_to_visit = node['children'] + nodes_to_visit

    return None


# {
#   'tag_name': 'h1',
#   'id': 'heading',
#   'text_content': 'Title',
#   'children': []
# }