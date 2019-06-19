"""
This module acts as main entry point
"""

from student import Anna, Luke

def main():
    """Create some students and do things"""
    
    anna = Anna()
    luke = Luke()

    anna.say_hello()
    luke.say_hello()

if __name__ == "__main__":
    main()