# Spla3 API (NSO App Version 2.5.0)<!-- omit in toc -->
### Added
|                      Name                      |            ID(sha256hash)             |
|:----------------------------------------------:|:-------------------------------------:|
| CoopRecordBigRunRecordContainerPaginationQuery |  `2b83817b6e88b202d25939fe04658d33`   |
|                CoopRecordQuery                 |  `b2f05c682ed2aeb669a86a3265ceb713`   |
|             CoopRecordRefetchQuery             |  `15035e6c4308b32d1a77e87398be5cd4`   |
|             useShareMyOutfitQuery              |  `3ba5572efce5bebbd859fc2d269d223c`   |


### ID changed
|                     Name                      |         ID(sha256hash) new          |         ID(sha256hash) old         |
|:---------------------------------------------:|:-----------------------------------:|:----------------------------------:|
|           CheckinWithQRCodeMutation           | `daffd9621680664dbf19d27e87484ac7`  | `8d54e1c6bdcc65181f65adc582914ad8` |
|    SupportButton_SupportChallengeMutation     | `991bace9e8c52d63084cd1570a97a5b4`  | `30aa261475d43bd765b4200fc67003c8` |
|                 CatalogQuery                  | `ff12098bad4989a813201b00ff22ac4e`  | `52504060c81ff2f2d618c4e5377e6e7c` |
|              CatalogRefetchQuery              | `60a6592c6ee8e47245020ae0d314d378`  | `4423dfd630867301fcdd834cd52922f4` |
|            CoopHistoryDetailQuery             | `379f0d9b78b531be53044bcac031b34b`  | `9ade2aa3656324870ccec023636aed32` |
|               CoopHistoryQuery                | `91b917becd2fa415890f5b47e15ffb15`  | `2fd21f270d381ecf894eb975c5f6a716` |
|           CoopPagerLatestCoopQuery            | `eb947416660e0a7520549f6b9a8ffcd7`  | `a2704e18852efce9cdbc61e205e1ed4e` |
|           DownloadSearchReplayQuery           | `8e904b52b5080b6f4b4448a50762362c`  | `43a5f23eec238d7ee827cc87f47f050c` |
|              HistoryRecordQuery               | `f09da9d24d888797fdfb2f060dbdf4ed`  | `32b6771f94083d8f04848109b7300af5` |
|           HistoryRecordRefetchQuery           | `d997d8e3875d50d3a1dc7e8a756e9e07`  | `57b1ccae6949c407e2df9bcad2a8e573` |
|                   HomeQuery                   | `22e2fa8294168003c21b00c333c35384`  | `dba47124d5ec3090c97ba17db5d2f4b3` |
|          JourneyChallengeDetailQuery          | `5a199948d059985bd758cc0175131f4a`  | `38e58b84376a2ad49ddbe4061b948455` |
|      JourneyChallengeDetailRefetchQuery       | `e7414c7a64bf80bb50ce21d5ccfde772`  | `8dc246933b1f4e26a6dfd251878cf786` |
|                  ReplayQuery                  | `e9cbaa835977b6c6de77ca7a4be15b24`  | `7ec830425971a0e0ff5b2a378455e38e` |
|     ReplayUploadedReplayListRefetchQuery      | `3bd200163e63bfff42ab60a244cac042`  | `1d1048e2af114e263a3c3d3ddd34bcb4` |
|                 SettingQuery                  | `73bd677ed986ad2cb7004ceabfff4d38`  | `61228d553e7463c203e05e7810dd79a7` |
|              StageScheduleQuery               | `011e394c0e384d77a0701474c8c11a20`  | `730cd98e84f1030d3e9ac86b6f1aae13` |
|    refetchableCoopHistory_coopResultQuery     | `50be9b694c7c6b99b7a383e494ec5258`  | `2a7f4335bcf586d904db85e75ba868c0` |

<br>

# Spla3 API (NSO App Version 2.4.0)<!-- omit in toc -->
#### For reference
I used `Spla3_API_Helper_Detailed.py` and sent all the requests below to Spla3 API and got the responses.<br>
Responses are saved in [/Spla3_API/SampleData](https://github.com/pistachiochoco/NSOAPIforSpla3/tree/main/Spla3_API/SampleData)
and [/Spla3_API/SampleDataWidget](https://github.com/pistachiochoco/NSOAPIforSpla3/tree/main/Spla3_API/SampleDataWidget).

## Table of Contents <!-- omit in toc -->
- [App API](#app-api)
  - [Query](#query)
    - [Queries (No parameter required)](#queries-no-parameter-required)
    - [Queries (Extra parameter required)](#queries-extra-parameter-required)
      - [Descriptor of Parameters](#descriptor-of-parameters)
    - [Refetch Queries](#refetch-queries)
      - [Descriptor of Parameters](#descriptor-of-parameters-1)
  - [Mutation](#mutation)
      - [Descriptor of Parameters](#descriptor-of-parameters-2)
  - [Responses of some queries (memo)](#responses-of-some-queries-memo)
- [Widget API](#widget-api)
  - [Query](#query-1)
      - [Descriptor of Parameters](#descriptor-of-parameters-3)


## App API
### Query 
#### Queries (No parameter required)
|                   Name                    |           ID(sha256hash)           |
|:-----------------------------------------:|:----------------------------------:|
|            useCurrentFestQuery            | `c0429fd738d829445e994d3370999764` |
| myOutfitCommonDataFilteringConditionQuery | `d02ab22c9dccc440076055c8baa0fa7a` |
|     myOutfitCommonDataEquipmentsQuery     | `d29cd0c2b5e6bac90dd5b817914832f8` |
|               XRankingQuery               | `d771444f2584d938db8d10055599011d` |
|           XBattleHistoriesQuery           | `6796e3cd5dc3ebd51864dc709d899fc5` |
|             WeaponRecordQuery             | `5f279779e7081f2d14ae1ddca0db2b6e` |
|            StageScheduleQuery             | `730cd98e84f1030d3e9ac86b6f1aae13` |
|             StageRecordQuery              | `f08a932d533845dde86e674e03bbb7d3` |
|               SettingQuery                | `61228d553e7463c203e05e7810dd79a7` | 
|                ReplayQuery                | `7ec830425971a0e0ff5b2a378455e38e` | 
|        RegularBattleHistoriesQuery        | `3baef04b095ad8975ea679d722bc17de` | 
|        PrivateBattleHistoriesQuery        | `8e5ae78b194264a6c230e262d069bd28` |
|              PhotoAlbumQuery              | `7e950e4f69a5f50013bba8a8fb6a3807` |
|         PagerLatestVsDetailQuery          | `0329c535a32f914fd44251be1f489e24` |
|              MyOutfitsQuery               | `81d9a6849467d2aa6b1603ebcedbddbe` |
|        LatestBattleHistoriesQuery         | `0176a47218d830ee447e10af4a287b3f` |
|                 HomeQuery                 | `dba47124d5ec3090c97ba17db5d2f4b3` |
|            HistoryRecordQuery             | `32b6771f94083d8f04848109b7300af5` |
|             HeroHistoryQuery              | `fbee1a882371d4e3becec345636d7d1c` |
|               GesotownQuery               | `a43dd44899a09013bcfd29b4b13314ff` | 
|              FriendListQuery              | `f0a8ebc384cf5fbac01e8085fbd7c898` |
|              FestRecordQuery              | `44c76790b68ca0f3da87f2a3452de986` |
|         CoopPagerLatestCoopQuery          | `a2704e18852efce9cdbc61e205e1ed4e` |
|             CoopHistoryQuery              | `2fd21f270d381ecf894eb975c5f6a716` |
|          ConfigureAnalyticsQuery          | `f8ae00773cc412a50dd41a6d9a159ddd` |
|               CheckinQuery                | `5d0d1b45ebf4e324d0dae017d9df06d2` |
|              ChallengeQuery               | `8a079214500148bf88a8fce1d7209b90` |
|               CatalogQuery                | `52504060c81ff2f2d618c4e5377e6e7c` |
|      BattleHistoryCurrentPlayerQuery      | `49dd00428fb8e9b4dde62f585c8de1e0` |
|        BankaraBattleHistoriesQuery        | `0438ea6978ae8bd77c5d1250f4f84803` |

#### Queries (Extra parameter required)

|                         Name                          |           ID(sha256hash)           |                                 Variables                                  | Note                     |
|:-----------------------------------------------------:|:----------------------------------:|:--------------------------------------------------------------------------:|--------------------------|
|                  XRankingDetailQuery                  | `ec7174376203f9901713e116075c5ecd` |                                    $id                                     | season ID                | 
|                 VsHistoryDetailQuery                  | `291295ad311b99a6288fc95a5c4cb2d2` |                                $vsResultId                                 | battle ID                |
|                  SaleGearDetailQuery                  | `6eb1b255b2cf04c08041567148c883ad` |                                $saleGearId                                 | sale gear ID in Gesotown |
|  RankingHoldersFestTeamRankingHoldersPaginationQuery  | `be2eb9e9b8dd680519eb59cc46c1a32b` |                                    $id                                     | fest ID (?)              |
|        PagerUpdateBattleHistoriesByVsModeQuery        | `094a9b44ff21e8c409d6046fc1af9dfe` | $isRegular<br/>$isBankara<br/>$isXBattle<br/>$isLeague<br/>$isPrivate<br/> | True or False            |
|                  MyOutfitDetailQuery                  | `d935d9e9ba7a5b6b5d6ece7f253304fc` |                                $myOutfitId                                 | my outfit ID             |
|                     JourneyQuery                      | `bc71fc0264f3f72256724b069f7a4097` |                                    $id                                     | challenge journey ID     |
|              JourneyChallengeDetailQuery              | `38e58b84376a2ad49ddbe4061b948455` |                                 $journeyId                                 | challenge journey ID     |
|               DownloadSearchReplayQuery               | `43a5f23eec238d7ee827cc87f47f050c` |                                   $code                                    |                          |
|                DetailVotingStatusQuery                | `53ee6b6e2acc3859bf42454266d671fc` |                                  $festId                                   | fest ID                  |
|                  DetailRankingQuery                   | `4869de13d0d209032b203608cb598aef` |                                  $festId                                   | fest ID                  |
|              DetailFestRecordDetailQuery              | `96c3a7fd484b8d3be08e0a3c99eb2a3d` |                                  $festId                                   | fest ID                  |
|                CoopHistoryDetailQuery                 | `9ade2aa3656324870ccec023636aed32` |                            $coopHistoryDetailId                            | coop ID                  |
|          DetailTabViewXRankingLfRefetchQuery          | `4e8b381ae6f9620443627f4eac3a2210` |                        $cursor, $first, $id, &page                         | id is season ID          |
|          DetailTabViewXRankingGlRefetchQuery          | `5f8f333770ed3c43e21b0121f3a86716` |                        $cursor, $first, $id, &page                         | id is season ID          |
|          DetailTabViewXRankingClRefetchQuery          | `68f99b7b02537bcb881db07e4e67f8dd` |                        $cursor, $first, $id, &page                         | id is season ID          |
|          DetailTabViewXRankingArRefetchQuery          | `eb69df6f2a2f13ab207eedc568f0f8b6` |                        $cursor, $first, $id, &page                         | id is season ID          |
|         DetailTabViewWeaponTopsLfRefetchQuery         | `d46f88c2ea5c4daeb5fe9d5813d07a99` |                            $cursor, $first, $id                            | id is season ID          |
|         DetailTabViewWeaponTopsGlRefetchQuery         | `b23468857c049c2f0684797e45fabac1` |                            $cursor, $first, $id                            | id is season ID          |
|         DetailTabViewWeaponTopsClRefetchQuery         | `8d3c5bb2e82d6eb32a37eefb0e1f8f69` |                            $cursor, $first, $id                            | id is season ID          |
|         DetailTabViewWeaponTopsArRefetchQuery         | `a6782a0c692e8076656f9b4ab613fd82` |                            $cursor, $first, $id                            | id is season ID          |

#####  Descriptor of Parameters
- **XRankingDetailQuery**: `id: WFJhbmtpbmdTZWFzb24tcDoy` (season ID)
  - from **XRankingQuery**: `["data"]["xRanking"]["currentSeason"]["id"]`
  - Note: this query only can fetch first 25 players each rule. **DetailedTabViewXRankingXXRefetchQuery** can fetch ranking26~500 players.
  - Also this query only can fetch weapon top players of shooter and roller. Other weapon top players can be fetched from **DetailTabViewWeaponTopsXXRefetchQuery**.
- **DetailTabViewXRankingAr(Cl,Gl,Lf)RefetchQuery**: 
  ```
  (example)
  "cursor": "MjU"
  "first": 25
  "id": "WFJhbmtpbmdTZWFzb24tcDoy"
  "page": 1
  ```
    - cursor: 
      - `null`: for 1~25 players in current page
      - `MjU`: for 26~50 
      - `NTA`: for 51~75
      - `NzU`: for 76~200
    - id: season ID
    - page: from `1` to `5` 
- **DetailTabViewWeaponTopsAr(Cl,Gl,Lf)RefetchQuery**:
  ```
  (example)
  "cursor": "MjU"
  "first": 25
  "id": "WFJhbmtpbmdTZWFzb24tcDoy"
  ```
    - cursor: 
      - `MjU`: チャージャー、スロッシャー、スピナー、マニューバー
      - `NTA`: マニューバー(クアッドだけ)、シェルター、ブラスター、フデ、ストリンガー、ワイパー
    - id: season ID 

<br>

- **VsHistoryDetailQuery**: `vsResultId: VnNIaXN0b3J5RGV0YWlsLXUtYWpjYWJhdHpxdXNyb2tleXBubW06UkVHVUxBUjoyMDIyMTExM1QxMzU3MDlfMTcyY2EzOTAtNzNlZC00MjBiLTg0NjItMWI3NjRlMjAwOTM1`
  - from **RegularBattleHistoriesQuery**, **PrivateBattleHistoriesQuery**, **BankaraBattleHistoriesQuery**, **XBattleHistoriesQuery**, 


- **CoopHistoryDetailQuery**: `coopHistoryDetailId: Q29vcEhpc3RvcnlEZXRhaWwtdS1hamNhYmF0enF1c3Jva2V5cG5tbToyMDIzMDEwNFQxMzUwMzVfZGJhYTUxMjYtYTBlYi00ZTFjLWI1MzMtYjU0NDIzOWVjZDY2`
  - from **CoopHistoryQuery**

<br>

- **MyOutfitDetailQuery**: `myOutfitId: TXlPdXRmaXQtdS1hamNhYmF0enF1c3Jva2V5cG5tbTox`
  - from **MyOutfitsQuery**


- **SaleGearDetailQuery**: `saleGearId: U2FsZUdlYXItMF8xNjczMzk1MjAwXzA`
  - from **GesotownQuery**

<br>

- **PagerUpdateBattleHistoriesByVsModeQuery**:
  ```
    (example)
    "isRegular": True,
    "isBankara": True,
    "isXBattle": False,
    "isLeague": False,
    "isPrivate": False
  ```

- **DetailFestRecordDetailQuery**: `festId: RmVzdC1KUDpKVUVBLTAwMDAy`, `RmVzdC1KUDpKVUVBLTAwMDA0`
- **DetailRankingQuery**: `festId: RmVzdC1KUDpKVUVBLTAwMDAy`
- **DetailVotingStatusQuery**: `festId: RmVzdC1KUDpKVUVBLTAwMDAy` (only available during fest(?))
  - from **FestRecordQuery**

<br>

- **JourneyChallengeDetailQuery**: `journeyId: Q2hhbGxlbmdlSm91cm5leS1qb3VybmV5XzE`
  - from **ChallengeQuery**
- **JourneyQuery**: `id: Q2hhbGxlbmdlSm91cm5leS1qb3VybmV5XzE`
  - from **ChallengeQuery**

<br>

#### Refetch Queries
If the original query needs extra parameter, the corresponding refetch query also need that parameter.

|                  Name                  |           ID(sha256hash)           |       Original Query        |
|:--------------------------------------:|:----------------------------------:|:---------------------------:|
|          XRankingRefetchQuery          | `5149402597bd2531b4eea04692d8bfd5` |        XRankingQuery        |
|       XRankingDetailRefetchQuery       | `2aac81b2ec56fb2d15ce3d6a2b625772` |     XRankingDetailQuery     |
|      XBattleHistoriesRefetchQuery      | `94711fc9f95dd78fc640909f02d09215` |    XBattleHistoriesQuery    |
|       WeaponRecordsRefetchQuery        | `6961f618fcef440c81509b205465eeec` |      WeaponRecordQuery      |
|    VsHistoryDetailPagerRefetchQuery    | `994cf141e55213e6923426caf37a1934` |    VsHistoryDetailQuery     |
|        StageRecordsRefetchQuery        | `2fb1b3fa2d40c9b5953ea1ae263e54c1` |      StageRecordQuery       |
|  ReplayUploadedReplayListRefetchQuery  | `1d1048e2af114e263a3c3d3ddd34bcb4` |         ReplayQuery         |
|   RegularBattleHistoriesRefetchQuery   | `4c95233c8d55e7c8cc23aae06109a2e8` | RegularBattleHistoriesQuery |
| refetchableCoopHistory_coopResultQuery | `2a7f4335bcf586d904db85e75ba868c0` |      CoopHistoryQuery       |
|   PrivateBattleHistoriesRefetchQuery   | `89bc61012dcf170d9253f406ebebee67` | PrivateBattleHistoriesQuery |
|         PhotoAlbumRefetchQuery         | `53fb0ad32c13dd9a6e617b1158cc2d41` |       PhotoAlbumQuery       |
|         MyOutfitsRefetchQuery          | `10db4e349f3123c56df14e3adec2ee6f` |     MyOutfitDetailQuery     |
|   LatestBattleHistoriesRefetchQuery    | `7161210aad0793e58e76f20e0443855e` | LatestBattleHistoriesQuery  |
|          JourneyRefetchQuery           | `09eee118fa16415d6bc3846bc6e5d8e5` |        JourneyQuery         |
|   JourneyChallengeDetailRefetchQuery   | `8dc246933b1f4e26a6dfd251878cf786` | JourneyChallengeDetailQuery |
|       HistoryRecordRefetchQuery        | `57b1ccae6949c407e2df9bcad2a8e573` |     HistoryRecordQuery      |
|        HeroHistoryRefetchQuery         | `4f9ae2b8f1d209a5f20302111b28f975` |      HeroHistoryQuery       |
|          GesotownRefetchQuery          | `951cab295eafdbeccfc2e718d7a98646` |        GesotownQuery        |
|         FriendListRefetchQuery         | `aa2c979ad21a1100170ddf6afea3e2db` |       FriendListQuery       |
|         FestRecordRefetchQuery         | `73b9837d0e4dd29bfa2f1a7d7ee0814a` |       FestRecordQuery       |
|   DetailFestVotingStatusRefethQuery    | `92f51ed1ab462bbf1ab64cad49d36f79` |   DetailVotingStatusQuery   |
|         DetailFestRefethQuery          | `18c7c465b18de5829347b7a7f1e571a1` | DetailFestRecordDetailQuery |
|     CoopHistoryDetailRefetchQuery      | `d3188df2fd4436870936b109675e2849` |   CoopHistoryDetailQuery    |
|         ChallengeRefetchQuery          | `34aedc79f96b8613501bba465295f779` |       ChallengeQuery        |
|          CatalogRefetchQuery           | `4423dfd630867301fcdd834cd52922f4` |        CatalogQuery         |
|   BankaraBattleHistoriesRefetchQuery   | `92b56403c0d9b1e63566ec98fef52eb3` | BankaraBattleHistoriesQuery |


#####  Descriptor of Parameters
- **XRankingDetailRefetchQuery**: Returns first 25 players of each rule in current page.
  ```
  (example)
  "id": "WFJhbmtpbmdTZWFzb24tcDoy"
  "pageAr": 5
  "pageCl": 1
  "pageGl": 1
  "pageLf": 1
  ```



### Mutation
|                   Name                   |           ID(sha256hash)           |    variables    |
|:----------------------------------------:|:----------------------------------:|:---------------:|
|       VotesUpdateFestVoteMutation        | `a2c742c840718f37488e0394cd6e1e08` |     $teamId     |
|          UpdateMyOutfitMutation          | `bb809066282e7d659d3b9e9d4e46b43b` |     $input      |
|  SupportButton_SupportChallengeMutation  | `30aa261475d43bd765b4200fc67003c8` |       $id       |
| SaleGearDetailOrderGesotownGearMutation  | `b79b7a101a243912754f72437e2ad7e5` |     $input      |
| ReplayModalReserveReplayDownloadMutation | `87bff2b854168b496c2da8c0e7f3e5bc` |     $input      |
|          CreateMyOutfitMutation          | `31ff008ea218ffbe11d958a52c6f959f` |     $input      |
|        CheckinWithQRCodeMutation         | `8d54e1c6bdcc65181f65adc582914ad8` | $checkinEventId |

##### Descriptor of Parameters
- **UpdateMyOutfitMutation**:
  ```
  "input": {
      "myOutfit": {
          "clothingGearId": 5023,
          "controlOptionConsole": {
              "cameraSpeedGyro": 0,
              "cameraSpeedStick": 5,
              "isEnableGyro": true,
              "isReverseLr": false,
              "isReverseUd": false
          },
          "controlOptionHandheld": {
              "cameraSpeedGyro": -1,
              "cameraSpeedStick": -1,
              "isEnableGyro": true,
              "isReverseLr": false,
              "isReverseUd": false
          },
          "headGearId": 21010,
          "id": "TXlPdXRmaXQtdS1hamNhYmF0enF1c3Jva2V5cG5tbTo0",
          "shoesGearId": 3024,
          "weaponId": 2030
      }
  }
  ```
<br>

- **SaleGearDetailOrderGesotownGearMutation**:
  ```
  "input": {
      "id": "U2FsZUdlYXItMV8xNjczNTEwNDAwXzA=",
      "isForceOrder": true
  }
  ```
  

<br><br>
### Responses of some queries (memo)
- **myOutfitCommonDataFilteringConditionQuery**: `weaponCategories`, `subWeapons`, `specialWeapons`, `gearPowers`, `brands`
- **myOutfitCommonDataEquipmentsQuery**: `weapons`(with paint points?), `headGears`, `clothingGears`, `shoesGears`
- **XRankingQuery**: the top player of each rule and the user's ranking information
- **StageScheduleQuery**: `regularSchedules`, `bankaraSchedules`, `xSchedules`, `leagueSchedules`, `coopGroupingSchedule`,
- **festSchedules**, `currentFest`, `currentPlayer`, `vsStages`(win rate of current user)
- **SettingQuery**: `currentPlayer`(name, icon)
- **HomeQuery**: `currentPlayer`(weapon), `banners`, `friends` , `footerMessages` 
- **ConfigureAnalyticsQuery**: `playHistory`
  - battleNumTotal
  - paintPointTotal
  - udemaeMax
  - xMatchRank

<br>


## Widget API
### Query
I got these 5 queries manually and I didn't find any file including them. # TODO

|       Name       |                           ID(sha256hash)                           | variable |
|:----------------:|:------------------------------------------------------------------:|:--------:|
|  CoopSchedules   | `f2924b9d93f7ff68670b6b0a91ab49370b7e23cf3d6a4e51a6dcc2940e86b023` |  $first  |
|   VsSchedules    | `f5131603b235edce2218e71c27ed0d35610cb78c48bb44aa88e98fb37ab08cd0` |  $first  |
| LatestVsResults  | `d167126ea863c00e3472fb3c2e9d9fbc37304d6168cd736e98c490288124f390` |          |
| LatestAlbumPhoto | `11c92e624146233078b7902b6f61a883c9aa5968744fb03676e8996c3529008a` |          | 
| CurrentEquipment | `6415729605742e57e4f627db2a5714ba38da0992ec91133b243bf517cd905369` |          |

#####  Descriptor of Parameters
- **CoopSchedules**: `first: 6`
- **VsSchedules**： `first: 6`
  - It can be changed to any number but there only 5 coop schedules and 12 vs schedules available.



