#SAIFIQBAL1628421
month_list = ("January":"1", "February":"2", "March":"3", "April":"4", "May":"5", "June":"6", "July":"7",
"August":"8", "September":"9", "October":"10", "November":"11", "December":"12")

input_file = open('C:\\Users\\Desktop\\inputDates.txt', 'r')
output_file = open('C:\\Users\\Desktop\\ParsedDates.txt', 'w')

for each in input_file:
    if each != "-1":
        lis = each.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]

            if month.lower() in month_list:
                comma = day[-1]
                if comma == ',':
                    day = day[:len(day) - 1]
                    month_number = month_list[month.lower()]
                    ans = month_number + "/" + day + "/"
                    year

                    output_file.write(ans)
                    output_file.write("\n")

                    output_file.close()
                    input_file.close()