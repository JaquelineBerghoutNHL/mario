from app import generate_pyramid

def test_pyramid():
    assert(generate_pyramid(3)) == "  #\n ##\n###"