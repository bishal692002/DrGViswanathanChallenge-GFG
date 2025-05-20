class Solution {
    // Function to sort an array of 0s, 1s, and 2s
    public void sort012(int[] arr) {
        // code here
        int z = 0;
        int o = 0;
        int t = 0;
        
        for(int i = 0; i < arr.length;i++){
            if(arr[i] == 0) z++;
            else if(arr[i] == 1) o++;
            else t++;
        }
        
        for(int i = 0; i < arr.length;i++){
            if(z > 0){
                arr[i] = 0;
                z--;
            }
            else if(o > 0){
                arr[i] = 1;
                o--;
            }
            else if(t > 0){
                arr[i] = 2;
                t--;
            }
        }
        
    }
}