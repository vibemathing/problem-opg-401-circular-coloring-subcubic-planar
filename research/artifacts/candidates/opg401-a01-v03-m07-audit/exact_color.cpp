// Candidate generator cross-check only. No table formula or external solver.
// Format: n m k Q mode; edges; k fixed vertex indices; Q rows of k colors.
// mode 0 counts ALL complete colorings; mode 1 returns the first (existence only).
#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <vector>
using U=std::uint32_t; using Count=std::uint64_t;
constexpr int MAXN=16; constexpr U ALL=(U(1)<<20)-1;
int n,m,k,Q,mode; std::array<std::vector<int>,MAXN> adj;
std::array<U,20> allowed; std::array<int,MAXN> color,first;
Count nodes; bool got;
Count search(std::array<U,MAXN> dom,U remaining) {
    ++nodes;
    if (!remaining) { if(!got){ first=color; got=true; } return 1; }
    int v=-1, sz=21;
    for(int i=0;i<n;++i) if(remaining&(U(1)<<i)) {
        int t=std::popcount(dom[i]); if(t==0)return 0;
        if(t<sz || (t==sz && (v<0 || adj[i].size()>adj[v].size()))) {v=i;sz=t;}
    }
    Count count=0; U choices=dom[v],rem=remaining&~(U(1)<<v);
    while(choices) {
        int c=std::countr_zero(choices); choices&=choices-1;
        auto next=dom; bool possible=true;
        for(int w:adj[v]) if(rem&(U(1)<<w)) {
            next[w]&=allowed[c]; if(!next[w]) {possible=false;break;}
        }
        if(possible) {
            color[v]=c; Count add=search(next,rem);
            if(std::numeric_limits<Count>::max()-count<add) throw std::runtime_error("overflow");
            count+=add; if(mode==1 && count)return 1;
        }
    }
    return count;
}
int main(){try {
    if(!(std::cin>>n>>m>>k>>Q>>mode) || n<1 || n>MAXN || m<0 || m>n*(n-1)/2 || k<1 || k>n || n-k>12 || Q<0 || Q>20000 || (mode!=0&&mode!=1)) throw std::runtime_error("header");
    bool edge[MAXN][MAXN]={};
    for(int i=0,u,v;i<m;++i) {
        if(!(std::cin>>u>>v)||u<0||v<0||u>=n||v>=n||u==v||edge[u][v])throw std::runtime_error("edge");
        edge[u][v]=edge[v][u]=true; adj[u].push_back(v);adj[v].push_back(u);
    }
    std::vector<int> fixed(k); U used=0;
    for(int &v:fixed){if(!(std::cin>>v)||v<0||v>=n||(used&(U(1)<<v)))throw std::runtime_error("fixed");used|=U(1)<<v;}
    for(int c=0;c<20;++c) for(int d=0;d<20;++d)if(7<=std::abs(c-d)&&std::abs(c-d)<=13)allowed[c]|=U(1)<<d;
    for(int row=0;row<Q;++row){
        color.fill(-1); first.fill(-1); got=false;nodes=0; std::array<U,MAXN> dom;dom.fill(ALL);
        for(int v:fixed){int c;if(!(std::cin>>c)||c<0||c>=20)throw std::runtime_error("color"); color[v]=c; dom[v]=U(1)<<c;}
        bool valid=true;
        for(int v:fixed)for(int w:adj[v]){
            dom[w]&=allowed[color[v]];if(color[w]>=0 && !(allowed[color[v]]&(U(1)<<color[w])))valid=false;
        }
        Count count=valid?search(dom,((U(1)<<n)-1)&~used):0;
        std::cout<<row<<' '<<count<<' '<<nodes;
        if(got) for(int i=0;i<n;++i)std::cout<<' '<<first[i];
        std::cout<<'\n';
    }
    std::string extra;if(std::cin>>extra)throw std::runtime_error("trailing data");
    return 0;
}catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
