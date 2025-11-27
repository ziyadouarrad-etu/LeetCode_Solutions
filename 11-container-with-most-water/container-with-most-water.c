int maxArea(int* height, int heightSize) {
    int area=0, i=0, j=heightSize-1, h;

    while (i<j){

        if (height[i]<height[j]) h=height[i++];
        else h=height[j--];

        if ((j-i+1)*h>area) area=(j-i+1)*h;
    }
    return area;
}