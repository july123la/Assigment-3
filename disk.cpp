#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAX_CYLINDERS = 5000;  
const int REQUEST_COUNT = 1000;


int fcfs(vector<int> &requests, int head) {
    int movement = 0;
    int current = head;

    for (int i = 0;i < REQUEST_COUNT; i++) {
        movement += abs(current - requests[i]);
        current = requests[i];
    }
    return movement;
}

int scan(vector<int> &requests, int head) {
    int movement = 0;
    int current = head;

    vector<int> left, right;

    for (int i = 0; i < REQUEST_COUNT; i++) {
        if (requests[i] < head) left.push_back(requests[i]);
        else right.push_back(requests[i]);
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    for (int i = 0; i < right.size(); i++) {
        movement += abs(current - right[i]);
        current = right[i];
    }

    if (right.size() > 0) {
        movement += abs(current - (MAX_CYLINDERS - 1)); 
        current = MAX_CYLINDERS - 1;
    }

    for (int i = left.size() - 1; i >= 0; i--) {
        movement += abs(current - left[i]);
        current = left[i];
    }

    return movement;
}

int cscan(vector<int> &requests, int head) {
    int movement = 0;
    int current = head;

    vector<int> left, right;

    for (int i = 0; i < REQUEST_COUNT; i++) {
        if (requests[i] < head) left.push_back(requests[i]);
        else right.push_back(requests[i]);
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    for (int i = 0; i < right.size(); i++) {
        movement += abs(current - right[i]);
        current = right[i];
    }

    if (left.size() > 0) {
        movement += abs(current - (MAX_CYLINDERS - 1)); 
        movement += (MAX_CYLINDERS - 1);              
        current = 0;

        for (int i = 0; i < left.size(); i++) {
            movement += abs(current - left[i]);
            current = left[i];
        }
    }

    return movement;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cout << "Usage: ./disk <initial_head_position>\n";
        return 1;
    }

    int head = atoi(argv[1]);

    if (head < 0 || head >= MAX_CYLINDERS) {
        cout << "Error: head position must be between 0 and " <<MAX_CYLINDERS - 1 << ".\n";
        return 1;
    }

    srand(time(NULL));

    vector<int> requests;
    requests.reserve(REQUEST_COUNT);

    for (int i = 0; i < REQUEST_COUNT; i++) {
        requests.push_back(rand() % MAX_CYLINDERS);
    }

    cout << "\n--- Disk Scheduling Results ---\n";
    cout << "Initial head position: " << head << endl;
    cout << "Total requests: " << REQUEST_COUNT << endl;

    cout << "\nFCFS   movement: " << fcfs(requests, head) << endl;
    cout << "SCAN   movement: " << scan(requests, head) << endl;
    cout << "C-SCAN movement: " << cscan(requests, head) << endl;

    return 0;
}
