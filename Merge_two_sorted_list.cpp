class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL && list2 == NULL) {
            return NULL;
        }
        if (list1 == NULL) {
            return list2;
        }
        if (list2 == NULL) {
            return list1;
        }

        ListNode* head = NULL;
        if (list1->val <= list2->val) {
            head = list1;
            list1 = list1->next;
        } else {
            head = list2;
            list2 = list2->next;
        }
        ListNode* curr = head;

        while(list1 != NULL && list2 != NULL){
            if(list1 -> val > list2 -> val){
                curr -> next = list2;
                list2 = list2 -> next;
            }
            else{
                curr -> next = list1;
                list1 = list1 -> next;
            }
            curr = curr -> next;
        }

        if(list1 == NULL){
            curr -> next = list2;
        }
        else{
            curr -> next = list1;
        }

        return head;
    }
};
