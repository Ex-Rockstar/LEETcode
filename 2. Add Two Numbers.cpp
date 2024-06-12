
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dumb = new ListNode();
        ListNode* ans = dumb;

        int tot =0;
        int carry = 0;

        while(l1 || l2 || carry){
            tot=carry;

            if(l1){
                tot+=l1->val;
                l1=l1->next;

            }
            if(l2){
                tot+=l2->val;
                l2= l2->next;
            }

            int num = tot%10;
            carry = tot/10;
            dumb-> next = new ListNode(num);
            dumb =dumb-> next;

        }

        return ans->next;

        
    }
};