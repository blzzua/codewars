# https://www.codewars.com/kata/545cff101288c1d2da0006fb

def pagination_text(page_number, page_size, total_products):
    from_ = ( page_number - 1) * page_size + 1
    to_ = min(total_products, page_number * page_size )
    return f'Showing {from_} to {to_} of {total_products} Products.'
