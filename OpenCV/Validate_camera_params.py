
import numpy as np

def validate_intrinsic_matrix(K, name="K"):
    #Validate intrinsic camera matrix
    if K.shape != (3, 3):
        print(f"{name} should be a 3x3 matrix.")
        return False
    if np.linalg.det(K) == 0:
        print(f"{name} has a determinant of zero, invalid camera matrix.")
        return False
    print(f"{name} is a valid intrinsic matrix.")
    return True

def validate_rotation_matrix(R, name="R"):
    """ Validate rotation matrix """
    if R.shape != (3, 3):
        print(f"{name} should be a 3x3 matrix.")
        return False
    identity_check = np.allclose(np.dot(R.T, R), np.eye(3), atol=1e-6)
    determinant_check = np.isclose(np.linalg.det(R), 1.0, atol=1e-6)
    if not identity_check:
        print(f"{name} is not orthonormal.")
        return False
    if not determinant_check:
        print(f"{name} determinant is not 1, invalid rotation matrix.")
        return False
    print(f"{name} is a valid rotation matrix.")
    return True

def validate_translation_vector(T, name="T"):
    """ Validate translation vector """
    if T.shape != (3,):
        print(f"{name} should be a 3-element vector.")
        return False
    print(f"{name} is a valid translation vector.")
    return True

# Define camera matrices (Replace with actual values from .dat files)
K_0 = np.array([[926.08, 0, 356.09], [0, 925.78, 355.25], [0, 0, 1]])
K_1 = np.array([[924.23, 0, 351.05], [0, 923.39, 359.21], [0, 0, 1]])

R_0 = np.array([[-0.0956, 0.9953, -0.0137], [-0.8586, -0.0755, 0.5071], [0.5037, 0.0603, 0.8618]])
T_0 = np.array([-2.738, 1.029, 16.787])

R_1 = np.array([[-0.9782, 0.2066, 0.0211], [-0.1277, -0.6787, 0.7232], [0.1638, 0.7047, 0.6903]])
T_1 = np.array([1.3811, 5.1981, 16.6694])

R_01 = np.array([[0.2989, 0.8350, -0.4620], [-0.6733, 0.5276, 0.5180], [0.6763, 0.1563, 0.7199]])
T_01 = np.array([9.0960, -5.8837, 6.2755])

# Run validations
validate_intrinsic_matrix(K_0, "K_0")
validate_intrinsic_matrix(K_1, "K_1")
validate_rotation_matrix(R_0, "R_0")
validate_translation_vector(T_0, "T_0")
validate_rotation_matrix(R_1, "R_1")
validate_translation_vector(T_1, "T_1")
validate_rotation_matrix(R_01, "R_01")
validate_translation_vector(T_01, "T_01")
