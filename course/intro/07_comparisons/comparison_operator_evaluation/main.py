def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = edward_height == alphonse_height
    is_winry_alphonse_same = alphonse_height == winry_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same
