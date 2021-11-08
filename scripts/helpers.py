import re
import matplotlib.pyplot as plt

def validate_defined_argument(argument_value, argument_name):
    """Validates if a given argument has a defined value (is not None)."""
    if argument_value is None:
        raise ValueError(f"The {argument_name} should be defined")

def get_empty_matrix(max_x, max_y):
    matrix = []

    for x in range(max_x+1):
        line = []
        
        for y in range(max_y+1):
            line.append(None)
            
        matrix.append(line)
    
    return matrix

def get_direction_matrix_for_navigation(mdp, policy):
    unicode_diretions = { 'west': u'\u2190', 'north': u'\u2191', 'east': u'\u2192', 'south': u'\u2193' }
    
    metadata = []
    xs = []
    ys = []
    
    for state in policy.keys():
        if not state.startswith('robot-at'):
            continue
            
        x_as_string, y_as_string = re.findall(r'\d+', state)
        x = int(x_as_string) - 1
        y = int(y_as_string) - 1
        direction = policy[state].replace('move-', '')
    
        xs.append(x)
        ys.append(y)
        metadata.append([state, x, y, unicode_diretions[direction] ])
    
    max_x = max(xs)
    max_y = max(ys)
    
    color_matrix = get_empty_matrix(max_y, max_x)
    value_matrix = get_empty_matrix(max_y, max_x)
    
    for metadata_info in metadata:
        state, x, y, direction = metadata_info
        
        color = 0
        if state in mdp.initial_states:
            color = 0.5
        
        if state in mdp.goal_states:
            color = 1
        
        inverse_x = max_x - x
        
        color_matrix[y][inverse_x] = color
        value_matrix[y][inverse_x] = direction
    
    return color_matrix, value_matrix

def plot_navigation_policy(mdp, policy, figsize=(8, 8)):
    color_matrix, value_matrix = get_direction_matrix_for_navigation(mdp, policy)

    fig, ax = plt.subplots(figsize=figsize)
    ax.matshow(color_matrix, cmap=plt.cm.Blues, alpha=0.3)

    for y in range(len(value_matrix)):
        for x in range(len(value_matrix[y])):
            ax.text(x=x, y=y, s=value_matrix[y][x], va='center', ha='center', size='xx-large')

    plt.show()

def plot_residuals(maximum_residuals_per_iteration, title = 'Resíduos totais'):
    y = maximum_residuals_per_iteration
    x = range(1, len(maximum_residuals_per_iteration) + 1)

    plt.ylabel('Resíduo')
    plt.xlabel('Iterações')
    plt.plot(x, y, 'r-')

    plt.title(title)
    plt.show()

def get_value_function_matrix_for_navigation(mdp, value_function):    
    metadata = []
    xs = []
    ys = []
    
    for state in value_function.keys():
        if not state.startswith('robot-at'):
            continue
            
        x_as_string, y_as_string = re.findall(r'\d+', state)
        x = int(x_as_string) - 1
        y = int(y_as_string) - 1
    
        xs.append(x)
        ys.append(y)
        metadata.append([state, x, y, value_function[state] ])
    
    max_x = max(xs)
    max_y = max(ys)
    
    color_matrix = get_empty_matrix(max_y, max_x)
    value_matrix = get_empty_matrix(max_y, max_x)
    
    for metadata_info in metadata:
        state, x, y, value = metadata_info
        
        color = 0
        if state in mdp.initial_states:
            color = 0.5
        
        if state in mdp.goal_states:
            color = 1
        
        inverse_x = max_x - x
        
        color_matrix[y][inverse_x] = color
        value_matrix[y][inverse_x] = round(value, 2)
    
    return color_matrix, value_matrix

def plot_navigation_value_function(mdp, value_function):
    color_matrix, value_matrix = get_value_function_matrix_for_navigation(mdp, value_function)

    fig, ax = plt.subplots()
    ax.matshow(color_matrix, cmap=plt.cm.Blues, alpha=0.3)

    for y in range(len(value_matrix)):
        for x in range(len(value_matrix[y])):
            ax.text(x=x, y=y, s=value_matrix[y][x], va='center', ha='center', size='xx-large')

    plt.show()