# Create a test case that compares two strings
# Create another test case that compares different numbers
# Use any unit testing framework from this week's lessons.
def test_compare(str1, str2):
    count1 = 0
    count2 = 0

    for i in range(len(str1)):
        if str1[i] >= "0" and str1[i] <= "9":
            count1 += 1

    for i in range(len(str2)):
        if str2[i] >= "0" and str2[i] <= "9":
            count2 += 1

    return count1 == count2


print(test_compare("123", "12345"))
print(test_compare("12345", "geeks"))
print(test_compare("12geeks", "geeks12"))
