import decorators

@decorators.benchmark
def create_list(num):
    return [i for i in range(num)]

if __name__ == "__main__":
    
    test_list = create_list(1000)
    
    print(test_list)
