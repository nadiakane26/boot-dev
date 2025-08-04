def get_avg_brand_followers(all_handles, brand_name):
  count = 0
  for handle_list in all_handles:
    for handle in handle_list:
      if brand_name in handle:
        count +=1
  return count / len(all_handles) 