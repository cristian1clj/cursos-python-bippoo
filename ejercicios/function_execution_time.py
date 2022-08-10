from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        
        time_elapsed = final_time - initial_time
        print(f"\n + Pasaron " + str(time_elapsed.total_seconds()) + " segundos\n")
        
    return wrapper