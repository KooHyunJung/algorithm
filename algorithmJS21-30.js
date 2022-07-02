// 프로그래머스 | k번째수
// https://programmers.co.kr/learn/courses/30/lessons/42748
// 수도코드 원본 유지, 이차 배열 commands 반복문 돌리기
function solution(array, commands) {
    var answer = [];
    for(let i = 0; i < commands.length; i++) {
        let arr = array.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=>a-b);
        answer.push(arr[commands[i][2]-1])
    }
    return answer;
}
// 다른 사람 풀이 - 좀 더 직관적인듯
function solution(array, commands) {
    return commands.map(v => {
        return array.slice(v[0] - 1, v[1]).sort((a, b) => a - b).slice(v[2] - 1, v[2])[0];
    });
}
console.log(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));



