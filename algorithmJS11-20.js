// 프로그래머스 | x만큼 간격이 있는 n개의 숫자
// https://programmers.co.kr/learn/courses/30/lessons/12954
// 수도코드
// 반복문 돌려서 배열에 하나씩 값 추가 
function solution(x, n) {
    var answer = [];
    for (let i = 1; i < n+1; i++) {
        answer.push(x * i);
    }
    return answer;
}
// 다른 사람 풀이
function solution(x, n) {
    return Array(n).fill(x).map((v, i) => (i + 1) * v)
}
// console.log(solution(-4, 2))
