from movie_client import MovieClient
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print('-----------------------------')
    print('      MOVIE SEARCH APP')
    print('-----------------------------')


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)

                results = client.perform_search()
                print(f'Found {len(results)} results.')
                for r in results:
                    print(f'{r.year} — {r.title}')
        except requests.exceptions.ConnectionError:
            print('ERROR: Cannot search, you network is down')
        except ValueError as ve:
            print(f'ERROR: Your search string is invalid: {ve}')
        except Exception as x:
            print(f'ERROR: {type(x)}')

    print('exiting...')


if __name__ == "__main__":
    main()
