class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        stack.push(-1);
        int maxLen = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ')') {
                // remove top element from stack
                if (!stack.isEmpty()) {
                    stack.pop();
                }

                // calculate the max length until now
                if (!stack.isEmpty()) {
                    maxLen = Math.max(maxLen, i - stack.peek());
                    continue;
                }
            }
            stack.push(i);
        }

        return maxLen;
}


}
