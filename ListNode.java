import javax.management.ListenerNotFoundException;

public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class remove_nth_node {
    public ListNode removeNt(ListNode head, int n) {
        ListNode h_length = head;
        int length = 0;
        for (int i = 0; h_length != null; i++){
            length++;
            h_length = h_length.next;
        }
        ListNode current = head;
        int target = 0;
        target = length - n;
        if (target == 0){
            return head.next;
        }
        length = 0;
        for (int i = 0; current != null; i++){
            length++;
            if (length == target){
                current.next = current.next.next;
                break;
            }else{
                current = current.next;
            }
        }
        return head;

    }

    public static void main(String[] args) {

    }
}