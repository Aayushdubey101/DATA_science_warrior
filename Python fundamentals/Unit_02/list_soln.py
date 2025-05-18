# Solutions for list exercises from list.txt (questions 1 to 20)

# 1. Declare an empty list
empty_list = []
print("1. Empty list:", empty_list)

# 2. Declare a list with more than 5 items
more_than_five = [1, 2, 3, 4, 5, 6]
print("2. List with more than 5 items:", more_than_five)

# 3. Find the length of your list
length = len(more_than_five)
print("3. Length of the list:", length)

# 4. Get the first item, the middle item and the last item of the list
first_item = more_than_five[0]
middle_item = more_than_five[len(more_than_five)//2]
last_item = more_than_five[-1]
print("4. First, middle, last items:", first_item, middle_item, last_item)

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["John Doe", 30, 5.9, "Single", "123 Main St"]
print("5. Mixed data types list:", mixed_data_types)

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print("6. IT companies list:", it_companies)

# 7. Print the list using print()
print("7. Print it_companies list:", it_companies)

# 8. Print the number of companies in the list
num_companies = len(it_companies)
print("8. Number of companies:", num_companies)

# 9. Print the first, middle and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print("9. First, middle, last companies:", first_company, middle_company, last_company)

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"
print("10. Modified companies list:", it_companies)

# 11. Add an IT company to it_companies
it_companies.append("Tesla")
print("11. After adding a company:", it_companies)

# 12. Insert an IT company in the middle of the companies list
middle_index = len(it_companies)//2
it_companies.insert(middle_index, "Netflix")
print("12. After inserting in the middle:", it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break
print("13. After changing one company to uppercase (except IBM):", it_companies)

# 14. Join the it_companies with a string '#; '
joined_companies = '#; '.join(it_companies)
print("14. Joined companies string:", joined_companies)

# 15. Check if a certain company exists in the it_companies list.
company_to_check = "GOOGLE"
exists = company_to_check in it_companies
print(f"15. Does {company_to_check} exist in the list? {exists}")

# 16. Sort the list using sort() method
it_companies.sort()
print("16. Sorted companies list:", it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print("17. Reversed companies list:", it_companies)

# 18. Slice out the first 3 companies from the list
first_three = it_companies[:3]
print("18. First 3 companies:", first_three)

# 19. Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print("19. Last 3 companies:", last_three)

# 20. Slice out the middle IT company or companies from the list
length = len(it_companies)
if length % 2 == 0:
    middle_companies = it_companies[length//2 - 1:length//2 + 1]
else:
    middle_companies = [it_companies[length//2]]
print("20. Middle company or companies:", middle_companies)
