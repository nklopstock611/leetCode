import java.util.ArrayList;

// Input
// ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
// [[], [1], [2], [], [3], []]
// Output
// [null, null, null, 1.5, null, 2.0]

// Explanation
// MedianFinder medianFinder = new MedianFinder();
// medianFinder.addNum(1);    // arr = [1]
// medianFinder.addNum(2);    // arr = [1, 2]
// medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
// medianFinder.addNum(3);    // arr[1, 2, 3]
// medianFinder.findMedian(); // return 2.0

class MedianFinder {

    private ArrayList<Integer> nums;

    public MedianFinder() {
        this.nums = new ArrayList<Integer>();
    }
    
    public void addNum(int num) {
        this.nums.add(num);
    }
    
    public double findMedian() {
        Integer middle = this.nums.size() / 2;
        double median = 0;
        if (this.nums.size() % 2 == 0) {
            median = (this.nums.get(middle - 1) + this.nums.get(middle)) / 2;
        }
        else {
            median = this.nums.get(middle - 1);
        }

        return median;
    }

    public static void main(String[] args) {
        String[] stream = {"MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"};
        int[] nums = null;
        MedianFinder obj = null;
        double median = 0;
        int i = 0;
        for (String data : stream) {
            if (data.equals("MedianFinder")) {
                obj = new MedianFinder();
            }
            else if (data.equals("addNum")) {
                //int num = nums[i][0];
                obj.addNum(3);
            }
            else if (data.equals("findMedian")) {
                median = obj.findMedian();
            }
            i ++;
        }

        System.out.println(median);        
    }
}
