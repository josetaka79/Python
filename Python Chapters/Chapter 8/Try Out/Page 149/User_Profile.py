# Define the function to build a user profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# Build a profile of yourself
my_profile = build_profile(
    'Josephine', 
    'Anucha', 
    age=22, 
    location='South Africa', 
    profession='Software Developer'
)

# Print the profile
print("\n--- User Profile ---")
for key, value in my_profile.items():
    print(f"{key}: {value}")