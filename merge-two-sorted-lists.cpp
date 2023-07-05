/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* mergeTwoLists(ListNode* l, ListNode* m) {

       if(l==NULL){
           return m;
       }
       if( m == NULL){
           return l;
       }
       if(l -> val <=m->val){
           l->next = mergeTwoLists(l->next,m);
           return l;
       }
       else{
           m->next = mergeTwoLists(l,m->next);
           return m;
       }
        
    }
};