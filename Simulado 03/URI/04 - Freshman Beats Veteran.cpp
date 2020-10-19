#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;


// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
long long merge(string arr[], int l, int m, int r) 
{ 
    long long swaps = 0;
    int n1 = m - l + 1; 
    int n2 = r - m; 
  
    // Create temp arrays  
    string L[n1], R[n2]; 
  
    // Copy data to temp arrays L[] and R[]  
    for(int i = 0; i < n1; i++)
        L[i] = arr[l + i]; 
    for(int j = 0; j < n2; j++) 
        R[j] = arr[m + 1 + j]; 
  
    // Merge the temp arrays back into arr[l..r] 
      
    // Initial index of first subarray 
    int i = 0;  
      
    // Initial index of second subarray 
    int j = 0;  
      
    // Initial index of merged subarray 
    int k = l; 
      
    while (i < n1 && j < n2) 
    { 
        if (L[i].compare(R[j]) < 0)  
        { 
            arr[k] = L[i]; 
            i++; 
        }
        else if (R[j].compare(L[i]) < 0)  
        { 
            arr[k] = R[j]; 
            j++; 
            swaps += (long long)(n1 - i);
        } else {
            arr[k] = L[i]; 
            i++; 
        }
        k++; 
    } 
  
    // Copy the remaining elements of 
    // L[], if there are any  
    while (i < n1)  
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    // Copy the remaining elements of 
    // R[], if there are any  
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    }

    return swaps;
} 
  
// l is for left index and r is  
// right index of the sub-array 
// of arr to be sorted */ 
long long mergeSort(string arr[], int l, int r) 
{ 
    long long swaps = 0;
    if (l < r) 
    { 
          
        // Same as (l+r)/2, but avoids  
        // overflow for large l and h 
        int m = l + (r - l) / 2; 
  
        // Sort first and second halves 
        swaps += mergeSort(arr, l, m); 
        swaps += mergeSort(arr, m + 1, r); 
  
        swaps += merge(arr, l, m, r); 
    } 
    return swaps;
} 

int main() {
    int n, i;
    string registrations[100000];
    long long swaps;

    cin >> n;

    for(i = 0; i < n; i++){
        cin >> registrations[i];
    }

    swaps = mergeSort(registrations, 0, n - 1);
    printf("%lld\n", swaps);

    return 0;
}