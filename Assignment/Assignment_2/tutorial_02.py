import math


# Function for mean.
def mean(first_list):
   try: 
     mean_value = 0
     p = len(first_list)

     if p > 0:
       for i in range(0, len(first_list)):
          mean_value = mean_value+first_list[i]
          mean_value = mean_value/p
   except:
     mean_value = 0

   return mean_value


# Function for sorting.
def sorting(first_list):
    n = len(first_list)
    sorted_list = []
    for i in range(0, n):
       sorted_list.append(first_list[i])

    for i in range(0, n-1):
       for j in range(0, n-i-1):
           if sorted_list[j] > sorted_list[j+1]:
               sorted_list[j], sorted_list[j +
                   1] = sorted_list[j+1], sorted_list[j]



    return sorted_list






# Function to compute median.
def median(first_list):
    n = len(first_list)
    if n > 0:
        first_list = sorting(first_list)
        if n%2 == 0:
            median_value = (first_list[n/2]+first_list[(n/2)-1])/2
        else:
            median_value = (first_list[(int)((n-1)/2)])
    else:
        median_value = 0



    return median_value




# Function to compute Standard deviation.
def standard_deviation(first_list):
    n = len(first_list)
    total = 0
    p = mean(first_list)

    if n > 0:
        for i in range(0, n):
            x = (first_list[i])-p
            x = x**2
            total = total + x
        standard_deviation_value = math.sqrt((total)/n)
    else:
        standard_deviation_value = 0

    return standard_deviation_value


# Function to compute variance.
def variance(first_list):
    variance_value = standard_deviation(first_list)
    variance_value = variance_value**2
    return variance_value


# Function to compute RMSE.
def rmse(first_list, second_list):
    n = len(first_list)
    total = 0
    if n > 0:
      for i in range(0, n):
        x = (int(first_list[i])-int(second_list[i]))
        x = x**2
        total = total+x
      rmse_value = total/n
    else:
        rmse_value = 0

    return rmse_value


# Function to compute mse.
def mse(first_list, second_list):
    p = rmse(first_list, second_list)

    mse_value = p**2

    return mse_value


# Function to compute mae.
def mae(first_list, second_list):
    n = len(first_list)
    if n > 0:
        total = 0
        for i in range(0, n):
            total = total + abs(first_list[i]-second_list[i])
        mae_value = total/n
    else:
        mae_value = 0

    return mae_value


# Function to compute NSE.
def nse(first_list, second_list):
    n = len(first_list)
    if n > 0:
        m1 = mean(first_list)
        p = variance(first_list)
        ans = 0
        if p > 0:
            for i in range(0, n):
                q1 = first_list[i]-second_list[i]
                q1 = pow(q1,2)
                ans = ans + q1

            result = ans/(p*n)
            nse_value = 1 - result
        else:
            nse_value = 0
    else:
        nse_value = 1

    return nse_value

def pcc(first_list, second_list):
    return 1


# Function to compute Pearson correlation coefficient.
def pcc(first_list, second_list):
    n = len(first_list)
    if n > 0:
        d1 = standard_deviation(first_list)
        d2 = standard_deviation(second_list)
        m1 = mean(first_list)
        m2 = mean(second_list)
        total = 0
        x = 0
        total1 = 0
        if d1 == 0 and d2 == 0:
            pcc_value = 1
        elif d1 == 0 and d2 != 0:
            for i in range(0, n):
                total = total + (second_list[i] - m2)
            pcc_value = (total)/(d2*(math.sqrt(n))
       # elif int(d2) == 0 and d1 > 0:
        #
        #       total=total + (first_list[i] - m1)
         #   pcc_value=(total)/(d1*(math.sqrt(n)))
        else:
            for i in range(0, n):
                total=(first_list[i] - m1)
                total1=(second_list[i] - m2)
                x=x + (total*total1)
            pcc_value=(x)/((d1*d2)*n)
    else:
        pcc_value=0


    return pcc_value



# Function to compute Skewness.
def skewness(first_list):
    n=len(first_list)

    if n > 0:
        p=standard_deviation(first_list)
        q=mean(first_list)
        total = 0
        if p > 0:
            for i in range(0, n):
                total=total + (first_list[i]-q)
            x = total
            x=x/p
            x=pow(x, 3)

            skewness_value=x/n
        else:
            skewness_value=1
    else:
         skewness_value=0
    return skewness_value




# Function to compute Kurtosis.
def kurtosis(first_list):
    n=len(first_list)

    if n > 0:
        p=standard_deviation(first_list)
        q=mean(first_list)
        if p > 0:
            total = 0
            for i in range(0, n):
                total=total + (first_list[i]-q)
            x = total
            x=x/p
            x=x**2
            x=x**2
            kurtosis_value=x/n
        else:
            kurtosis_value=1
    else:
         kurtosis_value=0
    return kurtosis_value





# Function to compute sum.
def summation(first_list):
    n=len(first_list)
    if n > 0:
        total = 0
        for i in range(0, n):
            total=total+first_list[i]
        summation_value=total/n
    else:
        summation_value=0
    return summation_value
