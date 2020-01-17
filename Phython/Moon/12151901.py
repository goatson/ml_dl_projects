from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request, time





url_1 = "https://www.youtube.com/watch?v=0egKOXHb65w&feature=emb_logo"
response_1 = urllib.request.urlopen(url_1)

soup_1 = BeautifulSoup(response_1, 'lxml')
# print(response_1)
body = soup_1.find('body')
# print(body)
comment_1 = body.select('#contents')

print(comment_1, "@@@@@@")
# title1 = title[0].get_text
# for comment in comment_1:
#     print(comment, "######")




<ytd-comments id="comments" class="style-scope ytd-watch-flexy">
    
    <paper-spinner-lite class="style-scope ytd-comments" aria-hidden="true"><!--css-build:shady--><div id="spinnerContainer" class="  style-scope paper-spinner-lite"><div class="spinner-layer style-scope paper-spinner-lite"><div class="circle-clipper left style-scope paper-spinner-lite"><div class="circle style-scope paper-spinner-lite"></div></div><div class="circle-clipper right style-scope paper-spinner-lite"><div class="circle style-scope paper-spinner-lite"></div></div></div></div></paper-spinner-lite>
    <ytd-item-section-renderer id="sections" initial-count="2" class="style-scope ytd-comments">
    
    
    <div id="header" class="style-scope ytd-item-section-renderer"><ytd-comments-header-renderer class="style-scope ytd-item-section-renderer">
    
    <div id="title" class="style-scope ytd-comments-header-renderer">
      <h2 id="count" class="style-scope ytd-comments-header-renderer">
        <yt-formatted-string class="count-text style-scope ytd-comments-header-renderer">댓글 479개</yt-formatted-string>
      </h2>
      <span id="sort-menu" class="style-scope ytd-comments-header-renderer"><yt-sort-filter-sub-menu-renderer class="style-scope ytd-comments-header-renderer">
    
    <paper-tooltip class="style-scope yt-sort-filter-sub-menu-renderer" role="tooltip" tabindex="-1" style="left: 137.078px; top: 1065.19px;"><!--css-build:shady-->

    <div id="tooltip" class="style-scope paper-tooltip hidden">
      댓글 정렬
    </div>
</paper-tooltip>
    <yt-dropdown-menu class="style-scope yt-sort-filter-sub-menu-renderer has-items">
    
    <paper-menu-button dynamic-align="" class="style-scope yt-dropdown-menu" role="group" aria-haspopup="true" horizontal-align="left" vertical-align="top" aria-disabled="false"><!--css-build:shady-->

    <div id="trigger" class="style-scope paper-menu-button">
      <paper-button id="label" class="dropdown-trigger style-scope yt-dropdown-menu" slot="dropdown-trigger" aria-expanded="false" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="댓글 정렬"><!--css-build:shady-->
        
          <yt-icon id="label-icon" class="style-scope yt-dropdown-menu"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M3 18h6v-2H3v2zM3 6v2h18V6H3zm0 7h12v-2H3v2z" class="style-scope yt-icon"></path>
        <path d="M0 0h24v24H0z" fill="none" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
          <div id="icon-label" class="style-scope yt-dropdown-menu">정렬 기준</div>
        <dom-if class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
        <dom-if class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
      </paper-button>
    </div>

    <iron-dropdown id="dropdown" class="style-scope paper-menu-button" horizontal-align="left" vertical-align="top" aria-disabled="false" aria-hidden="true" style="outline: none; display: none;"><!--css-build:shady-->

    <div id="contentWrapper" class="style-scope iron-dropdown">
      <div slot="dropdown-content" class="dropdown-content style-scope paper-menu-button">
        <paper-listbox id="menu" class="dropdown-content style-scope yt-dropdown-menu" slot="dropdown-content" role="listbox" tabindex="0"><!--css-build:shady-->

    
        
          <a class="yt-simple-endpoint style-scope yt-dropdown-menu iron-selected" aria-selected="true" tabindex="0">
            <paper-item class="style-scope yt-dropdown-menu" role="option" tabindex="0" aria-disabled="false"><!--css-build:shady-->
    
              <paper-item-body class="style-scope yt-dropdown-menu"><!--css-build:shady-->

    
                <div class="item style-scope yt-dropdown-menu">인기 댓글순</div>
                <div secondary="" id="subtitle" class="style-scope yt-dropdown-menu" hidden="">
                  
                </div>
              
</paper-item-body>
              
                <yt-reload-continuation class="style-scope yt-dropdown-menu">
                </yt-reload-continuation>
              <dom-if restamp="" class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
              <dom-if restamp="" class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
            
</paper-item>
          </a>
        
          <a class="yt-simple-endpoint style-scope yt-dropdown-menu" tabindex="-1" aria-selected="false">
            <paper-item class="style-scope yt-dropdown-menu" role="option" tabindex="0" aria-disabled="false"><!--css-build:shady-->
    
              <paper-item-body class="style-scope yt-dropdown-menu"><!--css-build:shady-->

    
                <div class="item style-scope yt-dropdown-menu">최근 날짜순</div>
                <div secondary="" id="subtitle" class="style-scope yt-dropdown-menu" hidden="">
                  
                </div>
              
</paper-item-body>
              
                <yt-reload-continuation class="style-scope yt-dropdown-menu">
                </yt-reload-continuation>
              <dom-if restamp="" class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
              <dom-if restamp="" class="style-scope yt-dropdown-menu"><template is="dom-if"></template></dom-if>
            
</paper-item>
          </a>
        <dom-repeat id="repeat" class="style-scope yt-dropdown-menu"><template is="dom-repeat"></template></dom-repeat>
      
</paper-listbox>
      </div>
    </div>
</iron-dropdown>
</paper-menu-button>
  </yt-dropdown-menu>
  </yt-sort-filter-sub-menu-renderer></span>
    </div>
    <div id="red-commenting-div" class="style-scope ytd-comments-header-renderer" hidden="">
      <yt-formatted-string id="red-commenting-text" class="style-scope ytd-comments-header-renderer"></yt-formatted-string>
    </div>
    <div id="alert" class="style-scope ytd-comments-header-renderer"></div>
    <div id="prefilled-dialog-header" class="style-scope ytd-comments-header-renderer"></div>
    <div id="simple-box" class="style-scope ytd-comments-header-renderer"><ytd-comment-simplebox-renderer class="style-scope ytd-comments-header-renderer">
    
    <yt-img-shadow id="author-thumbnail" height="40" width="40" class="style-scope ytd-comment-simplebox-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="day every" height="40" width="40" src="//lh5.googleusercontent.com/-NtA-fQhH7ek/AAAAAAAAAAI/AAAAAAAAAAA/ACHi3rf1-h368HfX6gljFQ4e0x75JimFgQ/s88/photo.jpg"></yt-img-shadow>
    <div id="placeholder-area" class="style-scope ytd-comment-simplebox-renderer">
      <yt-formatted-string id="simplebox-placeholder" role="textbox" tabindex="0" class="style-scope ytd-comment-simplebox-renderer">공개적으로 댓글을 남길 계정: <span class="bold style-scope yt-formatted-string">day every</span></yt-formatted-string>
    </div>
    <div id="attachments" class="style-scope ytd-comment-simplebox-renderer">
      <div id="image-button" class="style-scope ytd-comment-simplebox-renderer"></div>
    </div>
    <div id="comment-dialog" class="style-scope ytd-comment-simplebox-renderer" hidden=""></div>
  </ytd-comment-simplebox-renderer></div>
    <div id="backstage-post-dialog" class="style-scope ytd-comments-header-renderer"></div>
    <div id="post-stream-filter" class="style-scope ytd-comments-header-renderer" hidden=""></div>
    <div id="zero-state-message" class="style-scope ytd-comments-header-renderer"></div>
    <div id="scheduling-zero-state-message" class="style-scope ytd-comments-header-renderer" hidden=""></div>
  </ytd-comments-header-renderer></div>
    <div id="spinner-container" class="style-scope ytd-item-section-renderer">
      <paper-spinner-lite class="style-scope ytd-item-section-renderer" aria-hidden="true"><!--css-build:shady--><div id="spinnerContainer" class="  style-scope paper-spinner-lite"><div class="spinner-layer style-scope paper-spinner-lite"><div class="circle-clipper left style-scope paper-spinner-lite"><div class="circle style-scope paper-spinner-lite"></div></div><div class="circle-clipper right style-scope paper-spinner-lite"><div class="circle style-scope paper-spinner-lite"></div></div></div></div></paper-spinner-lite>
    </div>
    <div id="contents" class="style-scope ytd-item-section-renderer"><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCmZWb2yNV33RSMM7bv2_d3A">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="이태원" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l78GFWRaBUH0lnQ_8dyZ0rmY4aGKcbKTxDFLxA=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCmZWb2yNV33RSMM7bv2_d3A">
              <span class="style-scope ytd-comment-renderer">
                이태원
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzS1NvgmhlGoGkmZ4Z4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">근데 저게 진짜 도박인게 실패하면 찬물 제대로임ㅋㅋㅋ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzS1NvgmhlGoGkmZ4Z4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 937개">
        937
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 937명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 937개">
        937
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button><paper-tooltip class="style-scope ytd-toggle-button-renderer" role="tooltip" tabindex="-1" style="left: 114.391px; right: auto; top: 1233.69px; bottom: auto;"><!--css-build:shady-->

    <div id="tooltip" class="style-scope paper-tooltip hidden">
      싫어요
    </div>
</paper-tooltip></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 18개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 18개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCAqO5o8MKGcu6J0FVn4WCYw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="디슷저슷디슷" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7_9XJXqjB2pdUP8b_loCvq1yQcBoAlhtPxa=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCAqO5o8MKGcu6J0FVn4WCYw">
              <span class="style-scope ytd-comment-renderer">
                디슷저슷디슷
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyWvIIORWvSzmJeRPR4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">이런 두뇌를 많이 쓰는 수준 있는 야구 플레이가 계속 되면 리그 수준이 진짜 많이 올라갈텐데</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyWvIIORWvSzmJeRPR4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 351개">
        351
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 351명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 351개">
        351
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 15개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 15개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCNES61IayidMmVysAS4jPXw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="라우브" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79mkw8Li7wAm5CYl9_LVrwxLXroN6SftOKIag=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCNES61IayidMmVysAS4jPXw">
              <span class="style-scope ytd-comment-renderer">
                라우브
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz5rKe3-9PM_j1bRyB4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">인터뷰에서 주루코치도 놀랐다고ㅋㅋ로진백 만지는게 습관인걸 알아서 작정하고 들어갔다고 ㄷ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz5rKe3-9PM_j1bRyB4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 46개">
        46
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 46명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 46개">
        46
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCySt3FVsB32VlP3IanqB9Rw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="ᄏ뾰롱이" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-2ONbuGe0qEMqfn2P0Bo6yWu8LcMLLJ5X0JA=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCySt3FVsB32VlP3IanqB9Rw">
              <span class="style-scope ytd-comment-renderer">
                ᄏ뾰롱이
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyfKMDPX_RGa7LbD3V4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">평소엔 식빵형인데 진짜 짜증나도 센스하나는 지리는거같음</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyfKMDPX_RGa7LbD3V4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 286개">
        286
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 286명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 286개">
        286
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 3개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 3개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC5Y50xA_a8D26YDKRp506UA">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="성진 • 4년 전" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-LBfwAPKIt0Oas35ItMKdsRUn2lfVghHQcYA=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC5Y50xA_a8D26YDKRp506UA">
              <span class="style-scope ytd-comment-renderer">
                성진 • 4년 전
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgykT31PiZ3TQKrkKX14AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">이제 저 투수들은 주자3루에있을때 신경 ㅈㄴ쓰일듯</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgykT31PiZ3TQKrkKX14AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 534개">
        534
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 534명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 534개">
        534
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 16개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 16개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC2PT87Ze0K5vjROqVdLibVg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="seung won Jung" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-Q6j-gprmp1sZnX2m4Hg2-9E0E-SB7JfL5AA=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC2PT87Ze0K5vjROqVdLibVg">
              <span class="style-scope ytd-comment-renderer">
                seung won Jung
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwfL6ufVB3ZKtYEeEV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">이걸 어제 테이블석에앉아서 실제로 직관한건 정말 레전드 오브 레전드..관객들 막 소리지르고 진짜 오재원의 센스하나는 인정해줘야한다..</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwfL6ufVB3ZKtYEeEV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 199개">
        199
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 199명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 199개">
        199
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCpNTQxfCPr9bfqqeFnjURgQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="애플" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79i7nnZdPI-KNC2zmtFkXX78ZH0Eq5OB2_dOg=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCpNTQxfCPr9bfqqeFnjURgQ">
              <span class="style-scope ytd-comment-renderer">
                애플
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyNxtqQYvN7bmm7boR4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">진짜 빠따만 살아나면 오재원은 야구신인데.. 두뇌나 센스플레이 그냥 진짜 대단하다</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyNxtqQYvN7bmm7boR4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 271개">
        271
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 271명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 271개">
        271
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 15개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 15개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCLYBITdSOcg56l3-LqDvzlg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" loaded="" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="주하" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l78YD6NIe1DAzpt5jD5P_rfthdYLqWJrWj5pLw=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCLYBITdSOcg56l3-LqDvzlg">
              <span class="style-scope ytd-comment-renderer">
                주하
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugye5H4pEaYiIM021RN4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">오재원은 다른팀이면 진짜 너무 짜증나는 선수인데
같은 팀일땐 이만한 선수가 없어...
야구센스는 진짜 좋아☺</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugye5H4pEaYiIM021RN4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 161개">
        161
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 161명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 161개">
        161
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 5개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 5개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCJmXxGQqGSfgvxL8d-cVcIg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="최형우쉬프트" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79J35aNivsgjeJ7DckivEs02FnVJ0xSJ2vdPQ=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCJmXxGQqGSfgvxL8d-cVcIg">
              <span class="style-scope ytd-comment-renderer">
                최형우쉬프트
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx5yHp40GRfYmHQba54AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">한국시리즈에서 보여줬으면 슼 선수들 멘탈 뒤집고도 남았을듯</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx5yHp40GRfYmHQba54AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 26개">
        26
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 26명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 26개">
        26
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCGfmDcicSNTfc20VDloSA_w">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="오늘TV" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-WG1VdgIQalZLZhwIsIdUL8PZGdPhyw8l7eQ=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCGfmDcicSNTfc20VDloSA_w">
              <span class="style-scope ytd-comment-renderer">
                오늘TV
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx67-s9EMQE9_a9nFF4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">진짜 오또라이 야구센스만큼은 우리나라 레전드임 양신 승엽신 보다 센스가좋음</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx67-s9EMQE9_a9nFF4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 59개">
        59
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 59명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 59개">
        59
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCzgcG2jjuswXsjQh90schow">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="김민석" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79RxsSBHzENDxVz4h3LW92wf-0zsAuRNp4SBQ=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCzgcG2jjuswXsjQh90schow">
              <span class="style-scope ytd-comment-renderer">
                김민석
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxTZcTpG-FSgSeZMXJ4AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">역시 재원이형 방망이는 죽었어도 센스는 죽지않았어!!</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxTZcTpG-FSgSeZMXJ4AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 85개">
        85
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 85명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 85개">
        85
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 8개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 8개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC_dNjIOYL98hkVSWsl_tdjg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="포돌이" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l78RxFQJUymyCNUUN8g08-BfEILhTAabFw1nOw=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC_dNjIOYL98hkVSWsl_tdjg">
              <span class="style-scope ytd-comment-renderer">
                포돌이
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwEi0hqJMYWYzPH4pB4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">오재원은 진짜 야구지능 하나는 대단함
상대팀이면 진짜 역겨운데 같은팀이면 ㅈ되게 든든한 선수지</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwEi0hqJMYWYzPH4pB4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 197개">
        197
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 197명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 197개">
        197
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 19개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 19개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCrX_gVubKaeYKEs3XYiu-Vw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="쥬피터s" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-1LD7lrr_aWau1o9Pa6EHvx9BBcfUaUNSW8A=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCrX_gVubKaeYKEs3XYiu-Vw">
              <span class="style-scope ytd-comment-renderer">
                쥬피터s
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxEcmzfgWTwhvZ-ES54AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">박경수 lg시절 홈스틸
차우찬 진해수
현재 LG</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxEcmzfgWTwhvZ-ES54AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 64개">
        64
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 64명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 64개">
        64
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 2개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 2개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCS_qdv4U7ZWVv10JPtvvRtA">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="K3RShaW 22" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-ZltDjTqqmhCp62THTAuptG1tPmc2rlFedgw=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCS_qdv4U7ZWVv10JPtvvRtA">
              <span class="style-scope ytd-comment-renderer">
                K3RShaW 22
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzlS9vzZiS7grl948t4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">이거보니까 작년  생각나네 스퀴즈번트 할려고 홈으로 최형우뛰었는데 와중에 타자는 번트 못대고 그걸또 포수는 못잡고 그래서 포일로 득점한 최형우.ㅋㅋ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzlS9vzZiS7grl948t4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 130개">
        130
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 130명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 130개">
        130
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 8개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 8개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC_cc_Krj1FVVtN1pY4W7mqg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="reo nah" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79d9T2D7vhBVtFGyYa0Sx0gxqUCnYMpuZDz8Q=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC_cc_Krj1FVVtN1pY4W7mqg">
              <span class="style-scope ytd-comment-renderer">
                reo nah
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyGDEj6ddc_UKEmrI54AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=185s">3:05</a> 
투수 견제상황도 아니고 
더블스틸 상황도 아니고 
투수 투구동작 굼뜬거 간파해서 
담번 루틴때 단독 홈스틸 파고들었다는건 

그냥 야구천재 오재원</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyGDEj6ddc_UKEmrI54AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 58개">
        58
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 58명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 58개">
        58
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 5개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 5개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCjBCJR5Ag_hcDPcV1UCqGtA">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="내이름은화장소고기먹고싶다" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l79Pf_BPwE2m2Fo9-fLa7qPreaVVZkndCKXQQg=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCjBCJR5Ag_hcDPcV1UCqGtA">
              <span class="style-scope ytd-comment-renderer">
                내이름은화장소고기먹고싶다
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugy5KG2Q5lMEgbd68hZ4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">진짜 미쳤다 타격만 올라오면 진짜 더 완벽할텐데ㅠㅠ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugy5KG2Q5lMEgbd68hZ4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 3명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCGlg1i6Qa0bkM4nHholcbUg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="안이경" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-aClvb5dEuPRJN7YKOm0D4MyUooQVDuUjX4w=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCGlg1i6Qa0bkM4nHholcbUg">
              <span class="style-scope ytd-comment-renderer">
                안이경
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz9jB4laCi2lvh2HmV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">생각해 보면 LG 에게 점수 준 투수들이 지금 LG에 있네?</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz9jB4laCi2lvh2HmV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 18개">
        18
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 18명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 18개">
        18
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCD-QOxzfENC5DGcwVv7Elrw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="D Kim" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l793iRyJZUv4lBmAs1ZJnDhjs2yaMmWbYsx_lw=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCD-QOxzfENC5DGcwVv7Elrw">
              <span class="style-scope ytd-comment-renderer">
                D Kim
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwRsozBn8bzDhVBG7t4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">투수 버릇 읽히는 순간 작살난다. 이제 3루에만 홈스틸 하려고 노릴거 아냐. 투구습관 바꿔야겠다.</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwRsozBn8bzDhVBG7t4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 13개">
        13
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 13명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 13개">
        13
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC9OkjZoTPOrXs4iqd0Giw6w">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="식탐" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7_04X3V2gtwNCuyZIrtxj4ORenCB0DdMIaOiA=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC9OkjZoTPOrXs4iqd0Giw6w">
              <span class="style-scope ytd-comment-renderer">
                식탐
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwQU5hUgxM4SKzznqt4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">홈스틸은 정말 정말 집에 가고싶은 마음이 간절한 3루 주자만이 할 수 있는 거</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwQU5hUgxM4SKzznqt4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 9개">
        9
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 9명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 9개">
        9
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC4Ze9-ZqdrtHtpIxaa2gWZQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition" style="background-color: transparent;" loaded=""><img id="img" class="style-scope yt-img-shadow" alt="신명철" height="40" width="40" src="https://yt3.ggpht.com/a/AGF-l7-nkCFuAfWRKbiBkJHDVskfjTdKw3og2uN6Lg=s48-c-k-c0xffffffff-no-rj-mo"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC4Ze9-ZqdrtHtpIxaa2gWZQ">
              <span class="style-scope ytd-comment-renderer">
                신명철
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzB8g9nDir1Boe7fAh4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=149s">2:29</a> ㅠㅠㅠㅠ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzB8g9nDir1Boe7fAh4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCQhYiuJMDH31biT2lsuzDMw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCQhYiuJMDH31biT2lsuzDMw">
              <span class="style-scope ytd-comment-renderer">
                윤정후
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz2rdvNSpIGhReAvs54AaABAg">1개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=144s">2:24</a>에 피하다생식기맞음...</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugz2rdvNSpIGhReAvs54AaABAg">1개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 3명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCn8qkJ-0NgNkF8l--i1ygZQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCn8qkJ-0NgNkF8l--i1ygZQ">
              <span class="style-scope ytd-comment-renderer">
                JIHOO CH
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzIKYAa0tOh70Wk2QV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">상대팀인 내가 봐도 센스만점이네 ㅋㅋ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzIKYAa0tOh70Wk2QV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 11개">
        11
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 11명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 11개">
        11
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCeNdEl242SjQIs7nkzAwt7A">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCeNdEl242SjQIs7nkzAwt7A">
              <span class="style-scope ytd-comment-renderer">
                호날두
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzUN-sA9wqbLtyrOrh4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">근데 재원이형 왜 대주자 됐냐ㅠㅠ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgzUN-sA9wqbLtyrOrh4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 2명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC0m-JaTVnXInbn5fV4raaow">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC0m-JaTVnXInbn5fV4raaow">
              <span class="style-scope ytd-comment-renderer">
                혁
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugxlx5i-dA_vFq-gbwN4AaABAg">1개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=85s">1:25</a> 진해수 선수의 5년 큰그림...</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugxlx5i-dA_vFq-gbwN4AaABAg">1개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCZv_xmjARbcO0MhGPWoLk4A">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCZv_xmjARbcO0MhGPWoLk4A">
              <span class="style-scope ytd-comment-renderer">
                두산늘응원해
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugy0nj3XszSnHgqLye14AaABAg">1개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">우리 오캡틴ㅠㅠㅠ❤너무 멋있고 대단하다 중말</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugy0nj3XszSnHgqLye14AaABAg">1개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCfSWHLFhSanT7COEPZ_Jzjw">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCfSWHLFhSanT7COEPZ_Jzjw">
              <span class="style-scope ytd-comment-renderer">
                전준호
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwvP7L-1OY40YSk0yl4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=90s">1:30</a> 호오오오오옴인!!!호민!!</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwvP7L-1OY40YSk0yl4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCvbZ7KP8GNzrg10tfk_LzYg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCvbZ7KP8GNzrg10tfk_LzYg">
              <span class="style-scope ytd-comment-renderer">
                TAMANA S
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwQmIeTUuwpzJ68FyB4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">홈스틸도 대단하지만 모라 로진백만지는 버릇 알는것도 대단</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgwQmIeTUuwpzJ68FyB4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 10개">
        10
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 10명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 10개">
        10
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCL3YkI4_jpBHNomUsA6jOpg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCL3YkI4_jpBHNomUsA6jOpg">
              <span class="style-scope ytd-comment-renderer">
                lim4837 _
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugzi179f-4VOZz1SYCV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">오재원은 진짜 레전드선수ㅋㅋㅋㅋㅋ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugzi179f-4VOZz1SYCV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 2명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCcWZPPrHgM6Wcs2--F7-Afg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCcWZPPrHgM6Wcs2--F7-Afg">
              <span class="style-scope ytd-comment-renderer">
                헤헤헤헤
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx8xbV7T2RfywSpsEJ4AaABAg">2개월 전(수정됨)</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=8s">0:08</a> 눈빛 살아있는것 보소ㅎㄷㄷ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx8xbV7T2RfywSpsEJ4AaABAg">2개월 전(수정됨)</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCKxbau2bQKTBnNW6Xp6EF7A">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCKxbau2bQKTBnNW6Xp6EF7A">
              <span class="style-scope ytd-comment-renderer">
                김영주
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugws-5MX2hwZhfb7hHl4AaABAg">2개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=87s">1:27</a> 진해수선수 LG에서 대뷔하고 여태까지 있는줄알았는데..</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugws-5MX2hwZhfb7hHl4AaABAg">2개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCsJz9kR-Qjc9N6YOm8bH8ow">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCsJz9kR-Qjc9N6YOm8bH8ow">
              <span class="style-scope ytd-comment-renderer">
                김보민
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxGhTTxb_8cJX4L9nF4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=142s">2:22</a> 거기....맞앚...다....</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxGhTTxb_8cJX4L9nF4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC3O9yCz3x5Hg17vgyeiGrxg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC3O9yCz3x5Hg17vgyeiGrxg">
              <span class="style-scope ytd-comment-renderer">
                김도영
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxhCGE5hzVXVh_fhvB4AaABAg">1개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">저때 진짜 오캡틴 엄청 욕 먹고 있었는데 그나마 저 홈스틸 덕분에 욕받이에서 조금 벗어날 수 있었죠.. 
오캡틴 야구 진짜 안풀릴 때 내 마음이 다 아팠는뎅..</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxhCGE5hzVXVh_fhvB4AaABAg">1개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCVOQuMtEGCoRvmMXqLScy8A">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCVOQuMtEGCoRvmMXqLScy8A">
              <span class="style-scope ytd-comment-renderer">
                ᄒ ᄒ
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxJpRNfKm2MDzFckUB4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/results?search_query=%23%EC%9E%84%EC%B0%BD%EC%9A%A9%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B%E3%85%8B">#임창용ㅋㅋㅋㅋㅋ</a></yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxJpRNfKm2MDzFckUB4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC8dsmNxXaDTEnUddW46oykQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC8dsmNxXaDTEnUddW46oykQ">
              <span class="style-scope ytd-comment-renderer">
                Changwoo Lee
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxlxpDG-Csb_50PPGZ4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">오~ 야구 재능 넘버원...!!! 오재원</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxlxpDG-Csb_50PPGZ4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCIUjh0TM7w5BLtLrhMP6T1Q">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCIUjh0TM7w5BLtLrhMP6T1Q">
              <span class="style-scope ytd-comment-renderer">
                Daniel Hwang
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugzr46gXN6KUo4CMOIZ4AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=82s">1:22</a> 정작 투수 진해수는 LG로 홈스틸 한 박경수는 KT로... <a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=115s">1:55</a> 차우찬도 정작 LG로...</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugzr46gXN6KUo4CMOIZ4AaABAg">3개월 전(수정됨)</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UChFd4CC8x_oBZQXRYR1F3dg">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UChFd4CC8x_oBZQXRYR1F3dg">
              <span class="style-scope ytd-comment-renderer">
                Ming 9
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxlIixaqHHSgISEngV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">근데 우희힝 대단함 사람들한테 거의 다 답글 달아주네</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxlIixaqHHSgISEngV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 27개">
        27
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 27명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 27개">
        27
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer"><ytd-comment-replies-renderer class="style-scope ytd-comment-thread-renderer">
    
    <div id="expander" class="style-scope ytd-comment-replies-renderer">
      <ytd-button-renderer id="more-replies" aria-expanded="false" noink="" class="more-button-exp style-scope ytd-comment-replies-renderer" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 5개 모두 보기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 10l5 5 5-5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 5개 모두 보기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <ytd-button-renderer id="less-replies" aria-expanded="true" noink="" class="less-button-exp style-scope ytd-comment-replies-renderer" hidden="" button-renderer="" is-paper-button-with-icon="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1"><paper-button id="button" class="style-scope ytd-button-renderer" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글 숨기기"><!--css-build:shady--><yt-icon class="style-scope ytd-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M7 14l5-5 5 5z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon><yt-formatted-string id="text" class="style-scope ytd-button-renderer">답글 숨기기</yt-formatted-string></paper-button></a></ytd-button-renderer>
      <div id="expander-contents" class="style-scope ytd-comment-replies-renderer" hidden="">
        <div id="loaded-replies" class="style-scope ytd-comment-replies-renderer">
          <dom-repeat initial-count="10" class="style-scope ytd-comment-replies-renderer"><template is="dom-repeat"></template></dom-repeat>
        </div>
        <div id="continuation" class="cont-button-exp style-scope ytd-comment-replies-renderer"><yt-next-continuation class="style-scope ytd-comment-replies-renderer">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation">답글 더보기</yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
        <yt-next-continuation id="fake-continuation" show-button="true" show-icon="true" class="cont-button-exp style-scope ytd-comment-replies-renderer" hidden="">
    
    
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    
      <paper-button class="style-scope yt-next-continuation" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
        <yt-icon icon="subdirectory_arrow_right" class="style-scope yt-next-continuation"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path fill="none" d="M0 0h24v24H0V0z" class="style-scope yt-icon"></path><path d="M19 15l-6 6-1.42-1.42L15.17 16H4V4h2v10h9.17l-3.59-3.58L13 9l6 6z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
        <yt-formatted-string class="style-scope yt-next-continuation"></yt-formatted-string>
      </paper-button>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation>
      </div>
    </div>
    <div id="teaser-replies" class="style-scope ytd-comment-replies-renderer"></div>
  </ytd-comment-replies-renderer></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCX-ZGoEq5Id55AQm3OylgeQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCX-ZGoEq5Id55AQm3OylgeQ">
              <span class="style-scope ytd-comment-renderer">
                Seungtae Baek
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugyko56j1xqa1B01mJ14AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">2007년부터 두산의 발야구 보면서 팬이 됨 ㅎ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugyko56j1xqa1B01mJ14AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 3명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 3개">
        3
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCKXOfe2KcaVaILx_UjrsrxQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCKXOfe2KcaVaILx_UjrsrxQ">
              <span class="style-scope ytd-comment-renderer">
                윤정현
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx0Ad-SQoL4BNP1uj14AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=152s">2:32</a> 그냥 슝하고 지나가네 ㅋㅋㅋㅋㅋ멈춰서 심판 판정이라도 보고 갘ㅋㅋㅋㅋㅋ</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=Ugx0Ad-SQoL4BNP1uj14AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 1명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 1개">
        1
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC8VtnAxn624joDnjMMlDOHQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UC8VtnAxn624joDnjMMlDOHQ">
              <span class="style-scope ytd-comment-renderer">
                민서니
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxIeEmXEcGeh_olj5p4AaABAg">1개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer"><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;t=80s">1:20</a> 부터 나오는 bgm 제목 아시는 분?</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgxIeEmXEcGeh_olj5p4AaABAg">1개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 0명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
        0
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer><ytd-comment-thread-renderer class="style-scope ytd-item-section-renderer">
    
    <ytd-comment-renderer id="comment" class="style-scope ytd-comment-thread-renderer" comment-style="unknown">
    
    <div id="body-inappropriate-reply" class="style-scope ytd-comment-renderer" hidden="">
      <div id="author-thumbnail-placeholder" class="style-scope ytd-comment-renderer"></div>
      <div id="inappropriate-alert" class="style-scope ytd-comment-renderer" hidden="">
        <span class="style-scope ytd-comment-renderer"></span>
        <span id="inappropriate-text-click" class="style-scope ytd-comment-renderer">VIEW</span>
      </div>
    </div>
    <div id="body" class="style-scope ytd-comment-renderer">
      <div id="author-thumbnail" class="style-scope ytd-comment-renderer">
        <a class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCwJIGfc4BnwZtzMizuGg1KQ">
          <yt-img-shadow fit="" height="40" width="40" class="style-scope ytd-comment-renderer no-transition empty" style="background-color: transparent;"><img id="img" class="style-scope yt-img-shadow" alt="" height="40" width="40"></yt-img-shadow>
        </a>
      </div>
      <div id="main" class="style-scope ytd-comment-renderer">
        <div id="header" class="style-scope ytd-comment-renderer">
          <div id="header-badge" class="style-scope ytd-comment-renderer" hidden="">
            <div id="linked-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
            <div id="pinned-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></div>
          </div>

          <div id="header-author" class="style-scope ytd-comment-renderer">
            <a id="author-text" class="yt-simple-endpoint style-scope ytd-comment-renderer" href="/channel/UCwJIGfc4BnwZtzMizuGg1KQ">
              <span class="style-scope ytd-comment-renderer">
                한빈
              </span>
            </a>
            <span id="author-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            <span id="sponsor-comment-badge" class="style-scope ytd-comment-renderer" hidden=""></span>
            
            <yt-formatted-string class="published-time-text above-comment style-scope ytd-comment-renderer" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyKb4cMbCTNENH0tkV4AaABAg">3개월 전</a></yt-formatted-string>
            <span id="author-reputation" class="style-scope ytd-comment-renderer"></span>
            <span id="sponsors-only-badge" class="style-scope ytd-comment-renderer" hidden=""></span>

            <span id="moderation-reason-divider" class="style-scope ytd-comment-renderer" hidden="">
              •
            </span>
            <span id="moderation-reason-text" class="style-scope ytd-comment-renderer" hidden="">
              
            </span>
          </div>
        </div>

        
        <ytd-expander id="expander" class="expander-exp style-scope ytd-comment-renderer" collapsed="" style="--ytd-expander-collapsed-height:80px;">
    
    <div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden="">
          </yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">야구도 망해가네 2017년까지만 했어도 자리꽉찻는데</yt-formatted-string>
    </div>
    
    <paper-button id="less" aria-expanded="true" noink="" class="style-scope ytd-expander" hidden="" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false"><!--css-build:shady-->
      <span slot="less-button" class="less-button-exp style-scope ytd-comment-renderer">간략히</span>
    </paper-button>
    <paper-button id="more" aria-expanded="false" noink="" class="style-scope ytd-expander" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" hidden=""><!--css-build:shady-->
      <span slot="more-button" class="more-button-exp style-scope ytd-comment-renderer">자세히 보기</span>
    </paper-button>
  </ytd-expander>
        
        <yt-formatted-string class="published-time-text below-comment style-scope ytd-comment-renderer" hidden="" has-link-only_=""><a class="yt-simple-endpoint style-scope yt-formatted-string" spellcheck="false" href="/watch?v=0egKOXHb65w&amp;lc=UgyKb4cMbCTNENH0tkV4AaABAg">3개월 전</a></yt-formatted-string>
        <ytd-comment-action-buttons-renderer id="action-buttons" class="style-scope ytd-comment-renderer" action-buttons-style="desktop-toolbar">
    
    <div id="toolbar" class="style-scope ytd-comment-action-buttons-renderer">
      <div id="reply-button" class="style-scope ytd-comment-action-buttons-renderer">
      </div>
      <span id="vote-count-left" class="style-scope ytd-comment-action-buttons-renderer" hidden="" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="like-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="나 외에 사용자 2명이 이 댓글을 좋아함" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M1 21h4V9H1v12zm22-11c0-1.1-.9-2-2-2h-6.31l.95-4.57.03-.32c0-.41-.17-.79-.44-1.06L14.17 1 7.59 7.59C7.22 7.95 7 8.45 7 9v10c0 1.1.9 2 2 2h9c.83 0 1.54-.5 1.84-1.22l3.02-7.05c.09-.23.14-.47.14-.73v-1.91l-.01-.01L23 10z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <span id="vote-count-middle" class="style-scope ytd-comment-action-buttons-renderer" aria-label="좋아요 2개">
        2
      </span>
      <ytd-toggle-button-renderer id="dislike-button" class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="true" is-icon-button="" has-no-text=""><a class="yt-simple-endpoint style-scope ytd-toggle-button-renderer" tabindex="-1" href="/create_channel?upsell=comment"><yt-icon-button id="button" class="style-scope ytd-toggle-button-renderer style-text size-default"><button id="button" class="style-scope yt-icon-button" aria-label="댓글 싫어요 표시" aria-pressed="false"><yt-icon class="style-scope ytd-toggle-button-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M15 3H6c-.83 0-1.54.5-1.84 1.22l-3.02 7.05c-.09.23-.14.47-.14.73v1.91l.01.01L1 14c0 1.1.9 2 2 2h6.31l-.95 4.57-.03.32c0 .41.17.79.44 1.06L9.83 23l6.59-6.59c.36-.36.58-.86.58-1.41V5c0-1.1-.9-2-2-2zm4 0v12h4V3h-4z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon></button></yt-icon-button></a></ytd-toggle-button-renderer>
      <div id="creator-heart" class="style-scope ytd-comment-action-buttons-renderer"></div>
      <div id="share-button" class="style-scope ytd-comment-action-buttons-renderer" hidden="">
      </div>
      <div id="reply-button-end" class="style-scope ytd-comment-action-buttons-renderer">
      <ytd-button-renderer class="style-scope ytd-comment-action-buttons-renderer style-text size-default" button-renderer="" is-paper-button=""><a class="yt-simple-endpoint style-scope ytd-button-renderer" tabindex="-1" href="/create_channel?upsell=comment_reply"><paper-button id="button" class="style-scope ytd-button-renderer style-text size-default" role="button" tabindex="0" animated="" elevation="0" aria-disabled="false" aria-label="답글"><!--css-build:shady--><yt-formatted-string id="text" class="style-scope ytd-button-renderer style-text size-default">답글</yt-formatted-string></paper-button></a></ytd-button-renderer></div>
    </div>
    <div id="reply-dialog" class="style-scope ytd-comment-action-buttons-renderer"></div>
  </ytd-comment-action-buttons-renderer>
        <div id="moderation-buttons" class="style-scope ytd-comment-renderer" hidden=""></div>
        <div id="view-hide-replies-buttons" class="style-scope ytd-comment-renderer" hidden="">
          <ytd-button-renderer id="view-threaded-replies" aria-expanded="false" noink="" class="style-scope ytd-comment-renderer" button-renderer=""></ytd-button-renderer>
          <ytd-button-renderer id="hide-threaded-replies" aria-expanded="true" noink="" class="style-scope ytd-comment-renderer" hidden="" button-renderer=""></ytd-button-renderer>
        </div>
      </div>

      <div id="action-menu" class="style-scope ytd-comment-renderer"><ytd-menu-renderer class="style-scope ytd-comment-renderer">
    
    <div id="top-level-buttons" class="style-scope ytd-menu-renderer"></div>
    <yt-icon-button id="button" class="dropdown-trigger style-scope ytd-menu-renderer"><button id="button" class="style-scope yt-icon-button" aria-label="작업 메뉴">
      <yt-icon class="style-scope ytd-menu-renderer"><svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;"><g class="style-scope yt-icon">
        <path d="M12 8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm0 2c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 6c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z" class="style-scope yt-icon"></path>
      </g></svg>
    
    
  </yt-icon>
    </button></yt-icon-button>
  </ytd-menu-renderer></div>
    </div>
    <div id="edit-dialog" class="style-scope ytd-comment-renderer" hidden=""></div>
  </ytd-comment-renderer>
    <div id="replies" class="style-scope ytd-comment-thread-renderer" hidden=""></div>
  </ytd-comment-thread-renderer></div>
    <div id="continuations" class="style-scope ytd-item-section-renderer"><yt-next-continuation class="style-scope ytd-item-section-renderer">
    
    
    
      <paper-spinner id="spinner" class="style-scope yt-next-continuation" aria-hidden="true"><!--css-build:shady--><div id="spinnerContainer" class="  style-scope paper-spinner"><div class="spinner-layer layer-1 style-scope paper-spinner"><div class="circle-clipper left style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div><div class="circle-clipper right style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div></div><div class="spinner-layer layer-2 style-scope paper-spinner"><div class="circle-clipper left style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div><div class="circle-clipper right style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div></div><div class="spinner-layer layer-3 style-scope paper-spinner"><div class="circle-clipper left style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div><div class="circle-clipper right style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div></div><div class="spinner-layer layer-4 style-scope paper-spinner"><div class="circle-clipper left style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div><div class="circle-clipper right style-scope paper-spinner"><div class="circle style-scope paper-spinner"></div></div></div></div></paper-spinner>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
    <dom-if class="style-scope yt-next-continuation"><template is="dom-if"></template></dom-if>
  </yt-next-continuation></div>
  </ytd-item-section-renderer>
  </ytd-comments>



