// 프로그래머스 | 부족한 예산 찾기
// https://programmers.co.kr/learn/courses/30/lessons/82612
// 가우스 공식
function solution(price, money, count) {
    const total = price * count * (count + 1) / 2 - money;
    return total > 0 ? total : 0;
}
// console.log(solution(3,20,4))



// 프로그래머스 | 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576
function solution1(participant, completion) {
    participant.sort();
    completion.sort();
    for(let i in participant) {
        if(participant[i] !== completion[i]) return participant[i];
    }
}
// console.log(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]))



// 프로그래머스 | 서울에서 김서방 찾기
// https://programmers.co.kr/learn/courses/30/lessons/12919
function solution2(seoul) {
    const kimIndex = seoul.indexOf("Kim");
    return `김서방은 ${kimIndex}에 있다`
}
// console.log(solution2(["Jane", "Kim"]))



// 프로그래머스 | 가장 큰 수
// https://programmers.co.kr/learn/courses/30/lessons/42746
function solution3(numbers) {
    let strNum = numbers.map(num => num + "");
    const answer = strNum.sort((a, b) => (b + a) - (a + b)).join("");
    return answer[0] === "0" ? "0" : answer;
}
// console.log(solution3([6, 10, 2]))



// 프로그래머스 | 예산
// https://programmers.co.kr/learn/courses/30/lessons/12982
function solution4(d, budget) {
    d.sort((a, b) => a - b);
    while (d.reduce((a, b) => (a + b), 0) > budget) {
    d.pop();
    }
    return d.length;
}
// console.log(solution4([2,2,3,3], 10))



// 프로그래머스 | 없는 숫자 더하기
// https://programmers.co.kr/learn/courses/30/lessons/86051
function solution5(numbers) {
    var answer = 45-numbers.reduce((acc,cur) => acc+cur);
    return answer;
}
function solution5(numbers) {
    return 45 - numbers.reduce((acc, cur) => acc + cur, 0);
}
console.log(solution5([1,2,3,4,6,7,8,0]))



// 프로그래머스 | 문자열 내 마음대로 정하기
// https://programmers.co.kr/learn/courses/30/lessons/12915
function solution6(strings, n) {
    var answer = [];
    return answer;
}
console.log(solution6(["sun", "bed", "car"], 1))