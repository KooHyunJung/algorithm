// 프로그래머스 | 부족한 예산 찾기
// https://programmers.co.kr/learn/courses/30/lessons/82612
// 가우스 공식
function solution(price, money, count) {
    const total = price * count * (count + 1) / 2 - money;
    return total > 0 ? total : 0;
}
console.log(solution(3,20,4))



// 프로그래머스 | 완주하지 못한 선수
// https://programmers.co.kr/learn/courses/30/lessons/42576
function solution1(participant, completion) {
    var answer = '';
    return answer;
}
console.log(solution1(["leo", "kiki", "eden"], ["eden", "kiki"]))
