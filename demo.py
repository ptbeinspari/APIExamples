
import asyncio
from examples import simple_api, rate_limiting, utils, pagination, error_and_retry_handling, batch, authentication

if __name__ == "__main__":

    print("Running demos ------------------------------")


    # Example usage - Simple Api
    # ---------------------------------------------------------------
    print("Running simple_api demo ----------- Started - GET")
    get_url = "https://pokeapi.co/api/v2/pokemon"
    getresult = asyncio.run(simple_api.get(get_url, "simple_get_result.json"))
    print("Running simple_api demo ----------- GET completed - saved to simple_get_result.json")
    
    print("Running simple_api demo ----------- Started - POST")
    post_url = "https://jsonplaceholder.typicode.com/posts"
    post_body = {
                    "name": "bulbasaur",
                    "type": "grass"
                }
    postresult = asyncio.run(simple_api.post(post_url, post_body, "simple_post_result.json"))
    print("Running simple_api demo ----------- POST completed - saved to simple_post_result.json")
    # # ---------------------------------------------------------------



    # # Example usage - Pagination
    # # ---------------------------------------------------------------
    # print("Running pagination demo ----------- Started")
    # asyncio.run(pagination.fetch_paginated("https://pokeapi.co/api/v2/pokemon?limit=20&offset=0"))
    # print("Running pagination demo ----------- Completed - all pages combined in one file")
    # # --------------------------------------------------------------- 




    # # Example usage - Batching
    # # ---------------------------------------------------------------
    # print("Running batch demo ----------- Started")
    # base_url = "https://jsonplaceholder.typicode.com/todos"
    # ids = [i for i in range(1,100)]
    # asyncio.run(batch.batch_fetch_ids(base_url, ids))
    # print(f"Running batch demo ----------- Completed - saved {len(ids)} JSON files")
    # # ---------------------------------------------------------------





    # # Example usage - Rate Limiting
    # # ---------------------------------------------------------------
    # print("Running rate_limiting demo ----------- (2 requests/s)...")
    # rate_calls_per_sec = 2
    # num_calls = 30
    # urls = [f"https://jsonplaceholder.typicode.com/todos/{i}" for i in range(1, num_calls+1)]
    # asyncio.run(rate_limiting.rate_limited_calls(urls, rate_calls_per_sec))
    # print(f"Running rate_limiting demo ----------- saved {len(urls)} files")
    # # ---------------------------------------------------------------




    # # Example usage - Error handling and retries
    # # ---------------------------------------------------------------
    # print("Running error_handling demo ----------- Started")
    # try:
    #     # This will fail but demonstrate retries
    #     asyncio.run(error_and_retry_handling.robust_api_call("https://httpstat.us/500")) # TimeoutError
    # except Exception as e:
    #     print(f"Running error_handling demo ----------- Completed with expected error after retries: {str(e.__class__)}")


    # try:
    #     asyncio.run(error_and_retry_handling.robust_api_call("https://pokeapi.co/api/v2/pokemon")) # No error
    #     print(f"Running error_handling demo ----------- Completed with expected result")
    # except Exception as e:
    #     print(f"Running error_handling demo ----------- Completed with expected error after retries: {str(e.__class__)}")
    # # ---------------------------------------------------------------





    # # Example usage - Authentication
    # # ---------------------------------------------------------------
    # print("Running authentication demo ----------- Started")
    
    # # Basic Auth (using a test endpoint)
    # asyncio.run(authentication.basic_auth_call(
    #         "https://httpbin.org/basic-auth/user/pass",
    #         "user",
    #         "pass"
    #     ))
    # print("Running authentication demo ----------- Basic auth example completed")
    
    # # OAuth (using a test endpoint)
    # asyncio.run(authentication.oauth_call(
    #         "https://httpbin.org/bearer",
    #         "test_token"
    #     ))
    # print("Running authentication demo ----------- OAuth example completed")
    # # ---------------------------------------------------------------