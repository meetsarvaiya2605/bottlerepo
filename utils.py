from passlib.context import CryptContext

# Create a CryptContext object to handle hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to hash the password
def hash_password(password: str):
    return pwd_context.hash(password)

# Function to verify a password (during login)
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
