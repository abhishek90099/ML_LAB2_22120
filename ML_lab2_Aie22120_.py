import math

def calculate_euclidean_distance(point1, point2):  # Function name changed
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimension")

    distance = 0  # Variable name changed
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)

def calculate_manhattan_distance(point1, point2):  # Function name changed
    if len(point1) != len(point2):
        raise ValueError("Points must have the same dimension")

    distance = 0  # Variable name changed
    for i in range(len(point1)):
        distance += abs(point1[i] - point2[i])
    return distance

def k_nearest_neighbors(training_data, test_instance, k):  # Function name and variable names changed
   
    distances = []
    for train_point, label in training_data:  # Variable name changed
        distance = calculate_euclidean_distance(train_point, test_instance)  # Function name changed
        distances.append((distance, label))
   
    distances.sort(key=lambda x: x[0])
   
    neighbors = distances[:k]
   
    class_votes = {}
    for _, label in neighbors:
        class_votes[label] = class_votes.get(label, 0) + 1
    
    return max(class_votes, key=class_votes.get)

def encode_labels(categories):  # Function name changed
   
    label_map = {}
    for i, category in enumerate(categories):
        label_map[category] = i
    return label_map

def one_hot_encode(categories):  # Function name changed
    
    unique_categories = list(set(categories))
    encoded_vectors = []
    for category in categories:
        encoded_vector = [0] * len(unique_categories)
        index = unique_categories.index(category)
        encoded_vector[index] = 1
        encoded_vectors.append(encoded_vector)
    return encoded_vectors

# main class
if __name__ == "__main__":
    # Euclidean distance
    point1 = [1, 4, 6]  # Variable name changed
    point2 = [2, 6, 8]  # Variable name changed
    print("Euclidean distance:", calculate_euclidean_distance(point1, point2))  # Function name changed

    # Manhattan distance
    print("Manhattan distance:", calculate_manhattan_distance(point1, point2))  # Function name changed

    # k-NN classifier
    training_data = [([1, 2], 'A'), ([2, 3], 'B'), ([3, 4], 'A')]
    test_instance = [1.5, 2.5]
    k = 2
    print("Predicted class label:", k_nearest_neighbors(training_data, test_instance, k))  # Function name changed

    # Label encoding
    categories = ['red', 'blue', 'green', 'red', 'green']
    print("Label encoding:", encode_labels(categories))  # Function name changed

    # One-Hot encoding
    print("One-Hot encoding:", one_hot_encode(categories))  # Function name changed
